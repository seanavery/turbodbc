import numpy as np

from opendbc.can.packer import CANPacker
from opendbc.car import DT_CTRL
from opendbc.car.common.pid import PIDController
from opendbc.car.body import bodycan
from opendbc.car.body.values import SPEED_FROM_RPM
from opendbc.car.interfaces import CarControllerBase

MAX_TORQUE = 500
MAX_TORQUE_RATE = 50
MAX_ANGLE_ERROR = np.radians(7)
MAX_POS_INTEGRATOR = 0.2   # meters
MAX_TURN_INTEGRATOR = 0.1  # meters


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
