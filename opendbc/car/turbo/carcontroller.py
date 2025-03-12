from opendbc.can.packer import CANPacker
from opendbc.car import Bus
from opendbc.car.interfaces import CarControllerBase

class CarController(CarControllerBase):
  def __init__(self, dbc_names, CP):
    super().__init__(dbc_names, CP)
    print("dbc_names: ", dbc_names)
    self.packer = CANPacker(dbc_names[Bus.main])

  def update(self, CC, CS, now_nanos):
    # print(CC)

    new_actuators = CC.actuators
    can_sends = []
    # if CC.enabled:
    if True:
      steering_val = self.normalize_steer(CC.actuators.torque)
      values = {
        "STEER_ANGLE": steering_val,
      }
      msg = self.packer.make_can_msg("STEER_CMD", 1, values)
      can_sends.append(msg)
      throttle_val = self.normalize_accel(CC.actuators.accel)
      values = {
        "THROTTLE": throttle_val,
      }
      msg = self.packer.make_can_msg("THROTTLE_CMD", 1, values)
      can_sends.append(msg)
    return new_actuators, can_sends

  # noramlize accel from (-4.0,4.0) to (-100, 100)
  def normalize_accel(self, accel):
    return int(accel * 25)

  # normalize steer from (-1.0, 1.0) to (60, 120)
  def normalize_steer(self, steer):
    return int(90 + steer * -30) # need to flip the sign
