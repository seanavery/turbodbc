from opendbc.car import Bus, CarSpecs, PlatformConfig, Platforms
from opendbc.car.structs import CarParams
from opendbc.car.docs_definitions import CarDocs
from opendbc.car.fw_query_definitions import FwQueryConfig, Request, StdQueries

Ecu = CarParams.Ecu

class CarControllerParams:
  def __init__(self, CP):
    pass

# GEAR_MAP = {
#   "DI_GEAR_INVALID": CarState.GearShifter.unknown,
#   "DI_GEAR_P": CarState.GearShifter.park,
#   "DI_GEAR_R": CarState.GearShifter.reverse,
#   "DI_GEAR_N": CarState.GearShifter.neutral,
#   "DI_GEAR_D": CarState.GearShifter.drive,
#   "DI_GEAR_SNA": CarState.GearShifter.unknown,
# }


class CAR(Platforms):
  TURBO_RC_CAR = PlatformConfig(
    [CarDocs("turbo rc car", package="All")],
    CarSpecs(mass=9, wheelbase=0.406, steerRatio=0.5, centerToFrontRatio=0.44),
    {Bus.main: 'turbo_rc_car'},
  )


FW_QUERY_CONFIG = FwQueryConfig(
  requests=[
    Request(
      [StdQueries.TESTER_PRESENT_REQUEST, StdQueries.UDS_VERSION_REQUEST],
      [StdQueries.TESTER_PRESENT_RESPONSE, StdQueries.UDS_VERSION_RESPONSE],
      bus=1,
    ),
  ],
)

DBC = CAR.create_dbc_map()
