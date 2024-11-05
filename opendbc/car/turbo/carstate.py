from opendbc.can.parser import CANParser
from opendbc.car import structs
from opendbc.car.interfaces import CarStateBase
from opendbc.car.turbo.values import DBC


class CarState(CarStateBase):
  def update(self, cp, *_) -> structs.CarState:
    ret = structs.CarState()
    return ret

  @staticmethod
  def get_can_parser(CP):
    messages = [
      ("TEST_MSG_1", 10),
    ]
    return CANParser(DBC[CP.carFingerprint]["pt"], messages, 0)
