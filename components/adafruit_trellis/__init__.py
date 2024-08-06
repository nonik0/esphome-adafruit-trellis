
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID

CODEOWNERS = ["@nonik0"]
DEPENDENCIES = ["binary_sensor", "switch", "i2c"]
AUTO_LOAD = ["binary_sensor", "switch"]
MULTI_CONF = True

adafruit_trellis_ns = cg.esphome_ns.namespace("adafruit_trellis")
AdafruitTrellis = adafruit_trellis_ns.class_(
    "AdafruitTrellis", cg.PollingComponent, i2c.I2CDevice
)

CONF_ADAFRUIT_TRELLIS_ID = "adafruit_trellis_id"
CONFIG_SCHEMA = (
    cv.Schema({cv.GenerateID(): cv.declare_id(AdafruitTrellis)})
    .extend(cv.polling_component_schema("30ms"))
    .extend(i2c.i2c_device_schema(0x70))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
