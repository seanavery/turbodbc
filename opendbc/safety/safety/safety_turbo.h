#pragma once

#include "safety_declarations.h"

static void turbo_rx_hook(const CANPacket_t *to_push) {
  UNUSED(to_push);
  // If receiving CAN msgs, assume controls allowed
  controls_allowed = true;
}

static bool turbo_tx_hook(const CANPacket_t *to_send) {
  UNUSED(to_send);

  // TODO: remove controls_allowed hardcode
  // used as hack to force controls allowed if not receiving can msgs
  controls_allowed = true;

  return true;
}

static safety_config turbo_init(uint16_t param) {
  static RxCheck turbo_rx_checks[] = {
    {.msg = {{0x205, 1, 1, .ignore_checksum = true, .ignore_counter = true, .frequency = 25U}, { 0 }, { 0 }}}, // CRUISE_ENABLE
    {.msg = {{0x208, 1, 2, .ignore_checksum = true, .ignore_counter = true, .frequency = 25U}, { 0 }, { 0 }}}, // STEER
    {.msg = {{0x209, 1, 2, .ignore_checksum = true, .ignore_counter = true, .frequency = 25U}, { 0 }, { 0 }}}, // STEER_16
  };

  static const CanMsg TURBO_TX_MSGS[] = {
    {0x202, 1, 2, .check_relay = false}, // steer
    {0x203, 1, 2, .check_relay = false}, // throttle
    {0x204, 1, 2, .check_relay = false}, // headlights
    {0x205, 1, 1, .check_relay = false}, // cruise
  };

  UNUSED(param);
  return BUILD_SAFETY_CFG(turbo_rx_checks, TURBO_TX_MSGS);
}

const safety_hooks turbo_hooks = {
  .init = turbo_init,
  .rx = turbo_rx_hook,
  .tx = turbo_tx_hook,
};
