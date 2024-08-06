import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import (
    ENTITY_CATEGORY_NONE,
    CONF_ID,
)

from . import CONF_ADAFRUIT_TRELLIS_ID, AdafruitTrellis


CODEOWNERS = ["@nonik0"]
DEPENDENCIES = ["adafruit_trellis"]

CONF_BUTTON_1 = "button_1"
CONF_BUTTON_2 = "button_2"
CONF_BUTTON_3 = "button_3"
CONF_BUTTON_4 = "button_4"
CONF_BUTTON_5 = "button_5"
CONF_BUTTON_6 = "button_6"
CONF_BUTTON_7 = "button_7"
CONF_BUTTON_8 = "button_8"
CONF_BUTTON_9 = "button_9"
CONF_BUTTON_10 = "button_10"
CONF_BUTTON_11 = "button_11"
CONF_BUTTON_12 = "button_12"
CONF_BUTTON_13 = "button_13"
CONF_BUTTON_14 = "button_14"
CONF_BUTTON_15 = "button_15"
CONF_BUTTON_16 = "button_16"

BUTTONS = [
    CONF_BUTTON_1,
    CONF_BUTTON_2,
    CONF_BUTTON_3,
    CONF_BUTTON_4,
    CONF_BUTTON_5,
    CONF_BUTTON_6,
    CONF_BUTTON_7,
    CONF_BUTTON_8,
    CONF_BUTTON_9,
    CONF_BUTTON_10,
    CONF_BUTTON_11,
    CONF_BUTTON_12,
    CONF_BUTTON_13,
    CONF_BUTTON_14,
    CONF_BUTTON_15,
    CONF_BUTTON_16
]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_ADAFRUIT_TRELLIS_ID): cv.use_id(AdafruitTrellis),
        cv.Optional(CONF_BUTTON_1): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_2): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_3): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_4): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_5): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_6): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_7): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_8): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_9): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_10): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_11): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_12): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_13): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_14): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_15): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_BUTTON_16): binary_sensor.binary_sensor_schema(
            entity_category=ENTITY_CATEGORY_NONE,
        )
    }
)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_ADAFRUIT_TRELLIS_ID])
    for i, key in enumerate(BUTTONS):
        if conf := config.get(key):
            sens = await binary_sensor.new_binary_sensor(conf)
            cg.add(hub.set_button_binary_sensor(i, sens)) # creates 0-indexing for buttons internally
