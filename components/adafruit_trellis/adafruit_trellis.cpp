#include "esphome/core/log.h"
#include "adafruit_trellis.h"

namespace esphome {
namespace adafruit_trellis {

static const char *TAG = "adafruit_trellis";

void AdafruitTrellis::setup() {
    ESP_LOGD(TAG, "Setting up Adafruit Trellis at address 0x%02x...", this->address_);

    this->write_bytes(HT16K33_OSCILLATOR_ON, nullptr, 0);
    this->blinkRate(HT16K33_BLINK_OFF);

    this->setBrightness(MAX_BRIGHTNESS);

    // int pin unused by integration currently
    this->write_bytes(HT16K33_INTERRUPT_ACTIVE_LOW, nullptr, 0);

    for (uint8_t i = 0; i < NUM_KEYS; i++)
        publish_initial_state_(this->buttons[i], false);

    ESP_LOGD(TAG, "Done setting up Adafruit Trellis");
}

void AdafruitTrellis::update() {
    if (this->readSwitches()) {
        for (uint8_t i = 0; i < NUM_KEYS; i++) {
            if (this->justPressed(i)) {
                ESP_LOGD(TAG, "Pressed: %d", i);
                publish_state_(this->buttons[i], true);
            }
            if (this->justReleased(i)) {
                ESP_LOGD(TAG, "Released: %d", i);
                publish_state_(this->buttons[i], false);
            }
        }

        this->writeDisplay();
    }
}

void AdafruitTrellis::set_button_binary_sensor(uint8_t k, binary_sensor::BinarySensor *button_binary_sensor) {
    this->buttons[k] = button_binary_sensor;
}

void AdafruitTrellis::set_led_state(uint8_t x, bool state) {
    ESP_LOGD(TAG, "LED %d = %d", x+1, state); // LED numbers are 1-indexed on YAML/UX side
    if (state)
        setLED(x);
    else 
        clrLED(x);
    writeDisplay();
}

void AdafruitTrellis::publish_initial_state_(binary_sensor::BinarySensor *binary_sensor, const bool &state) {
    if (binary_sensor == nullptr)
        return;

    binary_sensor->publish_initial_state(state);
}

void AdafruitTrellis::publish_state_(binary_sensor::BinarySensor *binary_sensor, const bool &state) {
    if (binary_sensor == nullptr)
        return;

    binary_sensor->publish_state(state);
}

void AdafruitTrellis::blinkRate(uint8_t b) {
    if (b > HT16K33_BLINK_HALFHZ) b = HT16K33_BLINK_OFF; // turn off if not sure
    this->write_bytes(HT16K33_BLINK_CMD | HT16K33_BLINK_DISPLAYON | (b << 1), nullptr, 0); 
}

void AdafruitTrellis::setBrightness(uint8_t b) {
    if (b > MAX_BRIGHTNESS) b = MAX_BRIGHTNESS;
    this->write_bytes(HT16K33_CMD_BRIGHTNESS | b, nullptr, 0);
}

bool AdafruitTrellis::readSwitches(void) {
    memcpy(lastKeys, keys, KEYS_BUF_LEN);

    this->read_register(HT16K33_KEYS_BASE_ADDR, keys, KEYS_BUF_LEN);
    for (uint8_t i = 0; i < KEYS_BUF_LEN; i++)
        if (lastKeys[i] != keys[i])
            return true;
    return false;
}

bool AdafruitTrellis::isKeyPressed(uint8_t k) {
    if (k > NUM_KEYS - 1) return false;
    k = ButtonLUT[k];
    return (keys[k>>4] & _BV(k & 0x0F));
}
bool AdafruitTrellis::wasKeyPressed(uint8_t k) {
    if (k > NUM_KEYS - 1) return false;
    k = ButtonLUT[k];
    return (lastKeys[k>>4] & _BV(k & 0x0F));
}

bool AdafruitTrellis::justPressed(uint8_t k) {
    return (isKeyPressed(k) & !wasKeyPressed(k));
}
bool AdafruitTrellis::justReleased(uint8_t k) {
    return (!isKeyPressed(k) & wasKeyPressed(k));
}

bool AdafruitTrellis::isLED(uint8_t x) {
    if (x > NUM_KEYS - 1) return false;
    x = LedLUT[x];
    return ((displayBuffer[x >> 4] & _BV(x & 0x0F)) > 0);
}
void AdafruitTrellis::setLED(uint8_t x) {
    if (x > NUM_KEYS - 1) return;
    x = LedLUT[x];
    displayBuffer[x >> 4] |= _BV(x & 0x0F);
}
void AdafruitTrellis::clrLED(uint8_t x) {
    if (x > NUM_KEYS - 1) return;
    x = LedLUT[x];
    displayBuffer[x >> 4] &= ~_BV(x & 0x0F);
}

void AdafruitTrellis::writeDisplay(void) {
    this->write_register(HT16K33_DISPLAY_BASE_ADDR, reinterpret_cast<const uint8_t *>(displayBuffer), DISP_BUF_LEN*2);
}

void AdafruitTrellis::dump_config(){
    ESP_LOGCONFIG(TAG, "Adafruit Trellis Config: I2C Addr: 0x%02x", this->address_);
}

}  // namespace adafruit_trellis
}  // namespace esphome