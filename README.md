# Internet of Things (IoT)

This repository contains an extensive exploration of IoT and IoT device. The repository includes information and research related to everything IoT along with personal projects. All projects and programs included here are based around the [Espressif ESP32-S2 development board](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/hw-reference/esp32s2/user-guide-devkitm-1-v1.html) and the [ESP-IDF Software Development Kit](https://www.espressif.com/en/products/sdks/esp-idf).

## Repository Structure
* [`wiki`](https://github.com/arshnooramin/internetofthings/wiki): Includes discussion, definitions, and explorations related to IoT and Networks
* `peripherals`: Exploration of ESP32 peripherals
  * `blink_red`: Program to blink RGB LED Red with a long (~1000 ms) delay
  * `rmt_servo`: Program to control a servo motor and RGB LED with an IR remote control
* `networks`: Implmentation of simple networking protocols for ESP32
  * `udp` and `tcp`: Establish a connection between ESP32 dev board (client) and a Windows PC (server) using UDP and TCP protocols
* `web_controller`: Program to use networking to create a web-based GUI controller for the ESP32-S2 GPIO
