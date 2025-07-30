from opendbc.can.packer import CANPacker
from opendbc.car import Bus, apply_std_steer_angle_limits
from opendbc.car.interfaces import CarControllerBase
from opendbc.car.turbo.values import CarControllerParams

class CarController(CarControllerBase):
  def __init__(self, dbc_names, CP):
    super().__init__(dbc_names, CP)
    print("dbc_names: ", dbc_names)
    self.packer = CANPacker(dbc_names[Bus.main])
    self.apply_angle_last = 0.0

  def update(self, CC, CS, now_nanos):
    actuators = CC.actuators
    can_sends = []

    if CC.enabled:
      # Apply steering angle limits and rate limiting
      # self.apply_angle_last = apply_std_steer_angle_limits(
      #   actuators.steeringAngleDeg,
      #   self.apply_angle_last,
      #   CS.out.vEgo,
      #   CS.out.steeringAngleDeg,
      #   CC.latActive,
      #   CarControllerParams.ANGLE_LIMITS
      # )

      self.apply_angle_last = CC.actuators.steeringAngleDeg
      steering_val = self.angle_to_servo(self.apply_angle_last)
      values = {
        "STEER_ANGLE": steering_val,
      }
      msg = self.packer.make_can_msg("STEER_CMD", 1, {"STEER_ANGLE": steering_val})
      if self.frame % 2 == 0:
        can_sends.append(msg)

    new_actuators = actuators.as_builder()
    new_actuators.steeringAngleDeg = self.apply_angle_last

    self.frame += 1

    return new_actuators, can_sends

  def angle_to_servo(self, steering_angle_deg):
    # normalize from (-180, 180) to (-18000, 18000)
    return int(steering_angle_deg * -100.0)

  # normalize accel from (-4.0,4.0) to (-100, 100)
  def normalize_accel(self, accel):
    return int(accel * 25)
