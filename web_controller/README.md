# Web-based GUI Controller for ESP32-S2 GPIO

## Purpose and Functionality
The purpose of this project is to begin developing an ESP32 based IoT oscilloscope. This project specifically allows the control of several GPIO pins on the ESP32 development board. The project allows the following functionalities:
* Set GPIO pins as INPUT or OUTPUT
* If GPIO set as input
  * Read the value on the set GPIO pin
* If GPIO set as output
  * Set the voltage on the set GPIO as HIGH (1) or LOW (0)
* Provides a web-based GUI (shown below) to allow users to perform the aforementioned functions

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
