from opendbc.can.parser import CANParser
from opendbc.car import Bus, DT_CTRL, create_button_events, structs
from opendbc.car.interfaces import CarStateBase
from opendbc.car.turbo.values import DBC

import time


ButtonType = structs.CarState.ButtonEvent.Type


class CarState(CarStateBase):
  def __init__(self, CP):
    super().__init__(CP)
    self.start_time = time.monotonic()
    self._button_sent = False
    self._prev_btn = 0

  def update(self, cp, *_) -> structs.CarState:
    ret = structs.CarState()
    elapsed = time.monotonic() - self.start_time
    ret.cruiseState.enabled = elapsed > 10
    ret.cruiseState.available = True
    ret.cruiseState.speed = 0.0

    ret.cruiseState.standstill = True
    # ret.steeringAngleDeg = 90.0
    ret.vEgo = 10.0

    ret.gearShifter = structs.CarState.GearShifter.drive

    # Simulate a resume button press once, after 10 seconds
    # cur_btn = 1 if elapsed > 10 and not self._button_sent else 0
    # if elapsed >10:
    #   ret.cruiseState.enabled = True
    # else:
    #   ret.cruiseState.enabled = False

    # buttons_dict = {1: ButtonType.resumeCruise}
    # ret.buttonEvents = create_button_events(cur_btn, self._prev_btn, buttons_dict)
    # self._prev_btn = cur_btn
    # if cur_btn == 1:
    #   self._button_sent = True


    return ret

  @staticmethod
  def get_can_parsers(CP):
    messages = [
    ]
    return {Bus.main: CANParser(DBC[CP.carFingerprint][Bus.main], messages, 0)}
