# esphome-adafruit-trellis

ESPHome component to monitor and control the [Adafruit Trellis](https://www.adafruit.com/product/1616) over I2C.

## Background

I wanted to make a fun blinky project that had a reasonable amount of utility with Home Assistant. I got a Trellis for the project, but I couldn't find any existing work to integrate the Trellis into ESPHome. I took the opportunity to learn how to write an ESPHome external component. The I2C control is mostly ported from [Adafruit's Trellis library](https://github.com/adafruit/Adafruit_Trellis_Library).

## Example Usage

See [trellis-minimal.yaml](/trellis-minimal.yaml) for an example minimal esphome YAML config that exposes all Trellis' buttons and LEDs.

See [trellis-example.yaml](/trellis-example.yaml) for an example esphome YAML config that can be configured to control 16 separate rooms/areas, one per button. Each button is associated with two entities: a switch that controls a room's lighting and a binary_sensor that reflects any motion in that room. Pressing a button will toggle the associated switch entity, and the button's LED will reflect the state. The state of the binary_sensor is also reflected with the LED which will blink when on, while still showing the state of the switch.

### Home Assistant integration ideas:
- use [template switches](https://www.home-assistant.io/integrations/switch.template/) to add more versatility to button presses, e.g. switch.turn_off will switch off all lights in a room, but switch.turn_on will only turn on a single primary light in the day or a night light at night.
- use [trigger-based binary sensors](https://www.home-assistant.io/integrations/template/#turning-an-event-into-a-trigger-based-binary-sensor) to transform binary_sensors on doors, windows, etc. into activity sensors that activate whenever they are opened or closed



## ~~Known~~ Potential Issues

Using a Trellis at the non-default address and/or using multiple Trellises is currently untested/unverified.