# Web-based GUI Controller for ESP32-S2 GPIO

## Purpose and Functionality
The purpose of this project is to begin developing an ESP32 based IoT oscilloscope. This project specifically allows the control of several GPIO pins on the ESP32 development board. The project allows the following functionalities:
* Set GPIO pins as INPUT or OUTPUT
* If GPIO set as input
  * Read the value on the set GPIO pin
* If GPIO set as output
  * Set the voltage on the set GPIO as HIGH (1) or LOW (0)
* Provides a web-based GUI (shown below) to allow users to perform the aforementioned functions

![Web-based GUI for Controlling ESP32-S2 GPIO](https://lh3.googleusercontent.com/d3LDfKCIeJ--nk-LrxBF_fi-SvJdQbx9CNTMu2lKN0jTC0hxrR5PlokjSBYlNR2jV6rrFY5cwxaszvg_fVUppd02j7OvfJQrxjBBdimFzeonpU3dSSB7J0ta5ajwMOA9aXZn2a_LtRXOyv0dkktKxmWS2KKWl1u8gKMTHSFyBjp0ACE29d3FLkBc1BjC6M4_6G1TmU3ZN9I_cTjrmVN9hs4nYSeEUAR-6caKBCdPZFm_MtoQGQ_4VHRdn-bLE2iThk4Qv5EKWPLCfqtOSkCYqde5b4yRSaKCabM8aR3tKRkv_Fr7i9JVU5QtRAkIDBdrEG805XtXIT9IZLzQ17FfdZGv8kS9RfJYQUydxMt0lX3-vi6PdJPR2WTCws8tSaPEz4diulCT7XH2UZKXFlEeWWRzBy6RBdjhwO5g1bG3S8-skA9_uN9Fv1x2KrJ4-uGAuwvfwTSk2d8kXw9N3xvgpD6plEhc6K2dPD27s22S8AQYIcPL4RbovwgN6MF0G2ptFNGEz7CUIYtAYRiK0Oe0i5HYV9aqZO2BJ33uBITzfcO-KY1T3-Nf6XirMxXaMUWyEoWe1Zxz6IcFJC4WzNQpAYhtZ-nhnFeK0CKbP5sMXKfoslHL4B_-Y9sv0jJFMmGsRfwQayLbFvAuQ0gOipL46K_tNudyuTmarGDqdnpMEIWt3ota53G01F6xX9THpgDwVc2kTSB2fiZPrjicQ3Jn5_w7kxLSXK3c4rUKQeE_7Wn080LaG38FY9A_7tc_WekkMsQdUaIo7iqnN8E73Uu7rOriGDN8pXRZsA=w1217-h548-no?authuser=0)

## Hardware Required
This project only uses a ESP32-S2 development board for its integral functionality however the following additional hardware can be used to test the functionalities of this project:
* ESP32 development board
* LEDs to test OUTPUT
* Buttons to test INPUT
* 220 ohm resistor

## How to Use Program?
This repository includes the code needed to run the program on a ESP32 board (compiled, flashed, and tested on ESP32-S2 board). This directory includes all the code necessary and can be cloned using the following commands:
```
mkdir web_controller && cd web_controller\n
git init
git remote add -f origin https://github.com/arshnooramin/internetofthings
git config core.sparseCheckout true
echo 'web_controller' >> .git/info/sparse-checkout
git pull origin master
```
In addition to the code in this repository, there is also need to clone the websockets library used in this project:
```
git clone https://github.com/Molorius/esp32-websocket components/websocket
```
## How Program Works?
This project makes use of the [lwIP Netconn based Websockets component](https://github.com/Molorius/esp32-websocket) by [@Molorius](https://github.com/Molorius/). The program contains a simple HTML/CSS and JavaScript website which is served by the ESP32-S2, everytime a browser connects to the website a client connection is made to the server (ESP32-S2). The user inputs are then recorded via DOM events on the frontend via JavaScript, this information is then sent to the server where the required user actions are performed. Data is sent back from the server to the client where it is presented to the user. 
