#pragma once

#include "safety_declarations.h"

static void turbo_rx_hook(const CANPacket_t *to_push) {
  UNUSED(to_push);
  // If receiving CAN msgs, assume controls allowed
  controls_allowed = true;
}

static bool turbo_tx_hook(const CANPacket_t *to_send) {
  UNUSED(to_send);
  return true;
}

static safety_config turbo_init(uint16_t param) {
  // Allow all incoming CAN msgs
  static RxCheck turbo_rx_checks[] = {};
  // THROTTLE_CMD and STEER_CMD allowed
  static const CanMsg TURBO_TX_MSGS[] = {{0x203, 1, 2}, {0x202, 1, 2}};

  UNUSED(param);
  return BUILD_SAFETY_CFG(turbo_rx_checks, TURBO_TX_MSGS);
}

const safety_hooks turbo_hooks = {
  .init = turbo_init,
  .rx = turbo_rx_hook,
  .tx = turbo_tx_hook,
  .fwd = default_fwd_hook,
};
