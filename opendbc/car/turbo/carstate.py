import time
from opendbc.can.parser import CANParser
from opendbc.car import Bus, DT_CTRL, create_button_events, structs
from opendbc.car.interfaces import CarStateBase
from opendbc.car.turbo.values import DBC

class CarState(CarStateBase):
  def __init__(self, CP):
    super().__init__(CP)

  def update(self, can_parsers) -> structs.CarState:
    cp = can_parsers[Bus.main]
    ret = structs.CarState()
    ret.cruiseState.enabled = cp.vl["CRUISE_ENABLE"]["ENABLE"] == 1
    ret.cruiseState.available = True
    ret.gearShifter = structs.CarState.GearShifter.drive
    ret.vEgo = cp.vl["SPEED"]["SPEED"]
    steer_angle = cp.vl["STEER_ANGLE"]["STEER_ANGLE"]
    # normalize steer angle from (0, 255) to (-90, 90)
    steer_angle = (steer_angle - 127.5) / 127.5 * 90.0
    ret.steeringAngleDeg = steer_angle

    return ret

  @staticmethod
  def get_can_parsers(CP):
    messages = [
      ("CRUISE_ENABLE", 25),
      ("STEER_ANGLE", 25),
      ("SPEED", 25),
      ("STEER_16", 25),
    ]
    return {Bus.main: CANParser(DBC[CP.carFingerprint][Bus.main], messages, 1)}

