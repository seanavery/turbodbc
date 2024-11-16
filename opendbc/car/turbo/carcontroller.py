import numpy as np

from opendbc.can.packer import CANPacker
from opendbc.car.interfaces import CarControllerBase

class CarController(CarControllerBase):
  def __init__(self, dbc_name, CP):
    super().__init__(dbc_name, CP)
    self.packer = CANPacker(dbc_name)

  def update(self, CC, CS, now_nanos):
    print(CC)
    if CC.enabled:
      print("CarController enabled")
    new_actuators = CC.actuators
    can_sends = []
    steering_val = self.normalize_steer(CC.actuators.steer)
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
    return int(90 + steer * 30)
