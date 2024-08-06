#pragma once

#include "esphome/components/switch/switch.h"
#include "../adafruit_trellis.h"

namespace esphome {
namespace adafruit_trellis {

class LedSwitch : public switch_::Switch, public Parented<AdafruitTrellis> {
    public:
        LedSwitch(uint8_t index) { ledNum = index; }

    protected:
        uint8_t ledNum;

        void write_state(bool state) override {
            this->publish_state(state);
            this->parent_->set_led_state(this->ledNum, state);
        }
};

}  // namespace adafruit_trellis
}  // namespace esphome
