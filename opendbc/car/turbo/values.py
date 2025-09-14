from opendbc.car import Bus, CarSpecs, PlatformConfig, Platforms, AngleSteeringLimits
from opendbc.car.structs import CarParams
from opendbc.car.docs_definitions import CarDocs
from opendbc.car.fw_query_definitions import FwQueryConfig, Request, StdQueries

Ecu = CarParams.Ecu

class CarControllerParams:
  ANGLE_LIMITS: AngleSteeringLimits = AngleSteeringLimits(
    180,
    ([0., 5., 25.], [40.0, 24.0, 3.2]),
    ([0., 5., 25.], [80.0, 32.0, 4.8]),
  )
  STEER_STEP = 2  # Angle command is sent at 50 Hz

class CAR(Platforms):
  TURBO_RC_CAR = PlatformConfig(
    [CarDocs("turbo rc car", package="All")],
    # Steering wheel range += 180 deg
    # Servo range += 30 deg
    # servo to wheel ratio = 3
    CarSpecs(mass=9, wheelbase=0.3302, steerRatio=180/30*3),
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
