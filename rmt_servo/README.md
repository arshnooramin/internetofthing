# Controlling a Servo-Motor and RGB Lights with IR Remote Control

## Purpose and Functionality
The purpose of this project is to control the built-in WS2812 RGB LED and an external SG-90 (or any generic) servo motor with an IR remote control. The remote control allows to set colors and brightness on the RGB LED and the angle of the servo.

## Peripherals
This project combines the functionalities of three ESP32 Peripherals into one project:
* RMT for IR Remote Control and WS2812 RGB LED
* LEDC PWM for Servo Control

## How to Use Program?
This repository includes the code needed to run the program on a ESP32 board (compiled, flashed, and tested on ESP32-S2 board)

### Hardware Required
* ESP32 development board
* WS2812 LED Strip
* SG-90 Servo Motor
* IR Remote Control
* IR Receiver

### Connection
NOTE: The pin configurations can be modified using the `menuconfig` or by editing the main source program `mcpwm_servo_control.c`
* GPIO5 -> Servo PWM signal
* GPIO18 -> WS2812 LED (Built-in)
* GPIO6 -> IR Receiver
 
## How Program Works?
The program works by using the RMT library to receive decoded data from the IR receiver when a button is pressed on the IR remote. Once the hex code for a valid button on the IR remote control is detected it sends a signal to the WS2812 LED or a PWM signal to the Servo.
