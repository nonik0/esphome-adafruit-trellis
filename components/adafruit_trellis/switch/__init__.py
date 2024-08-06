import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from esphome.const import (
    ENTITY_CATEGORY_NONE,
    CONF_ID,
)

from .. import CONF_ADAFRUIT_TRELLIS_ID, AdafruitTrellis, adafruit_trellis_ns

CODEOWNERS = ["@nonik0"]
DEPENDENCIES = ["adafruit_trellis"]

CONF_LED_1 = "led_1"
CONF_LED_2 = "led_2"
CONF_LED_3 = "led_3"
CONF_LED_4 = "led_4"
CONF_LED_5 = "led_5"
CONF_LED_6 = "led_6"
CONF_LED_7 = "led_7"
CONF_LED_8 = "led_8"
CONF_LED_9 = "led_9"
CONF_LED_10 = "led_10"
CONF_LED_11 = "led_11"
CONF_LED_12 = "led_12"
CONF_LED_13 = "led_13"
CONF_LED_14 = "led_14"
CONF_LED_15 = "led_15"
CONF_LED_16 = "led_16"

LEDS = [
    CONF_LED_1,
    CONF_LED_2,
    CONF_LED_3,
    CONF_LED_4,
    CONF_LED_5,
    CONF_LED_6,
    CONF_LED_7,
    CONF_LED_8,
    CONF_LED_9,
    CONF_LED_10,
    CONF_LED_11,
    CONF_LED_12,
    CONF_LED_13,
    CONF_LED_14,
    CONF_LED_15,
    CONF_LED_16
]

LedSwitch = adafruit_trellis_ns.class_("LedSwitch", switch.Switch)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_ADAFRUIT_TRELLIS_ID): cv.use_id(AdafruitTrellis),
        cv.Optional(CONF_LED_1): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_2): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_3): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_4): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_5): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_6): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_7): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_8): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_9): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_10): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_11): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_12): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_13): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_14): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_15): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        ),
        cv.Optional(CONF_LED_16): switch.switch_schema(
            LedSwitch,
            entity_category=ENTITY_CATEGORY_NONE,
        )
    }
)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_ADAFRUIT_TRELLIS_ID])
    for i, key in enumerate(LEDS):
        if conf := config.get(key):
            s = await switch.new_switch(conf, i)
            await cg.register_parented(s, config[CONF_ADAFRUIT_TRELLIS_ID])
