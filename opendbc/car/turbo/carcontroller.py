import numpy as np

from opendbc.can.packer import CANPacker
from opendbc.car.interfaces import CarControllerBase

class CarController(CarControllerBase):
  def __init__(self, dbc_name, CP):
    super().__init__(dbc_name, CP)
    self.packer = CANPacker(dbc_name)

  def update(self, CC, CS, now_nanos):
    if CC.enabled:
      print("CarController enabled")
      # create actuator
    new_actuators = CC.actuators
    can_sends = []
    # create can msg
    values = {
      "STEER_ANGLE": 90,
      "STEER_ENABLE": 1,
    }
    print(self.packer)
    msg = self.packer.make_can_msg("STEER_CMD", 1, values)
    can_sends.append(msg)
    return new_actuators, can_sends
