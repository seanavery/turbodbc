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
    actuators = CC.actuators.as_builder()
    # create can sends
    can_sends = []

    return actuators, can_sends
