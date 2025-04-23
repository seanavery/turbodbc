#!/usr/bin/env python3
import unittest

from opendbc.car.structs import CarParams
import opendbc.safety.tests.common as common
from opendbc.safety.tests.libsafety import libsafety_py
from opendbc.safety.tests.common import CANPackerPanda

class TestTurbo(common.PandaSafetyTest):
  TX_MSGS = [[0x203, 1], [0x202, 1]]
  FWD_BUS_LOOKUP = {}

  def setUp(self):
    self.packer = CANPackerPanda("turbo_rc_car")
    self.safety = libsafety_py.libsafety
    self.safety.set_safety_hooks(CarParams.SafetyModel.turbo, 0)
    self.safety.init_tests()

  def test_fwd_hook(self):
    print("skipping fwd_hook test")

  def test_tx_hook(self):
    # create throttle message
    values = {"THROTTLE": 0}
    msg = self.packer.make_can_msg_panda("THROTTLE_CMD", 1, values)
    # create steering message
    # values = {"STEERING": 0}
    # msg2 = self.packer.make_can_msg_panda("STEERING_CMD", 1, values)
    self.safety.set_controls_allowed(True)
    self.assertTrue(self._tx(msg))
    self.assertTrue(self._tx(msg))
    # self.assertTrue(self._tx(msg2))

    # check that we can't send a message when controls are not allowed
    # self.safety.set_controls_allowed(False)
    # self.assertFalse(self._tx(common.make_msg(0, 0x203, 8)))
    # self.assertFalse(self._tx(common.make_msg(0, 0x202, 8)))


if __name__ == "__main__":
  unittest.main()