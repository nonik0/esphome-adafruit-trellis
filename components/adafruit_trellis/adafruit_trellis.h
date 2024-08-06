
// ported from https://github.com/adafruit/Adafruit_Trellis_Library
#pragma once

#include "esphome/core/component.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/switch/switch.h"
#include "esphome/components/i2c/i2c.h"

#ifndef _BV
#define _BV(bit) (1 << (bit))
#endif

namespace esphome {
namespace adafruit_trellis {

// full spec: https://cdn-shop.adafruit.com/datasheets/ht16K33v110.pdf

// I2C register lookup tables
static const uint8_t
  LedLUT[16] =
    { 0x3A, 0x37, 0x35, 0x34,
      0x28, 0x29, 0x23, 0x24,
      0x16, 0x1B, 0x11, 0x10,
      0x0E, 0x0D, 0x0C, 0x02 },
  ButtonLUT[16] =
    { 0x07, 0x04, 0x02, 0x22,
      0x05, 0x06, 0x00, 0x01,
      0x03, 0x10, 0x30, 0x21,
      0x13, 0x12, 0x11, 0x31 };

static const uint8_t LED_ON   = 1;
static const uint8_t LED_OFF  = 0;
static const uint8_t NUM_KEYS = 16;
static const uint8_t MAX_BRIGHTNESS = 15;
static const uint8_t KEYS_BUF_LEN = 6;
static const uint8_t DISP_BUF_LEN = 8;

static const uint8_t HT16K33_BLINK_CMD       = 0x80;
static const uint8_t HT16K33_BLINK_DISPLAYON = 0x01;
static const uint8_t HT16K33_CMD_BRIGHTNESS  = 0xE0;
static const uint8_t HT16K33_OSCILLATOR_ON  = 0x21;
static const uint8_t HT16K33_INTERRUPT_ACTIVE_LOW = 0xA1;
static const uint8_t HT16K33_DISPLAY_BASE_ADDR = 0x00;
static const uint8_t HT16K33_KEYS_BASE_ADDR = 0x40;

static const uint8_t HT16K33_BLINK_OFF    = 0;
static const uint8_t HT16K33_BLINK_2HZ    = 1;
static const uint8_t HT16K33_BLINK_1HZ    = 2;
static const uint8_t HT16K33_BLINK_HALFHZ = 3;

class AdafruitTrellis : public i2c::I2CDevice, public PollingComponent {
  public:
    void setup() override;
    void update() override;
    void dump_config() override;

    void set_button_binary_sensor(uint8_t k, binary_sensor::BinarySensor *button_binary_sensor);
    void set_led_state(uint8_t x, bool state);

  protected:
    binary_sensor::BinarySensor *buttons[NUM_KEYS];

    void publish_initial_state_(binary_sensor::BinarySensor *binary_sensor, const bool &state);
    void publish_state_(binary_sensor::BinarySensor *binary_sensor, const bool &state);

  private:
    uint8_t keys[KEYS_BUF_LEN], lastKeys[KEYS_BUF_LEN];
    uint16_t displayBuffer[DISP_BUF_LEN];

    void blinkRate(uint8_t b);
    void setBrightness(uint8_t b);

    bool readSwitches(void);
    bool isKeyPressed(uint8_t k);
    bool wasKeyPressed(uint8_t k);
    bool justPressed(uint8_t k);
    bool justReleased(uint8_t k);

    void writeDisplay(void);
    bool isLED(uint8_t x);
    void setLED(uint8_t x);
    void clrLED(uint8_t x);
};


}  // namespace adafruit_trellis
}  // namespace esphome