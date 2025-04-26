from opendbc.can.parser import CANParser
from opendbc.car import Bus, structs
from opendbc.car.interfaces import CarStateBase
from opendbc.car.turbo.values import DBC


class CarState(CarStateBase):
  def update(self, cp, *_) -> structs.CarState:
    ret = structs.CarState()
    ret.cruiseState.enabled = True
    ret.cruiseState.available = True

    return ret

  @staticmethod
  def get_can_parsers(CP):
    messages = [
    ]
    return {Bus.main: CANParser(DBC[CP.carFingerprint][Bus.main], messages, 0)}
