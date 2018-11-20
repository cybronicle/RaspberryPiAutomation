#!/usr/bin/env python
from ServoPi import PWM
from ServoPi import Servo

#Pulse Width Modulation(PWM) instatiation
pwm = PWM(0x40)
#Sets the PWM to a frequency of 200 Hz
pwm.set_pwm_freq(200)
#Alloww the output to be displayed
pwm.output_enable()
#Setting the channel for data stream to 1, time period to 1024 out of 4095.
pwm.set_pwm(1,0,1024)

#Instantiation of the servo object
servo = Servo(0x40)
#setting frequency for the PWM to interact with the PWM object
servo.set_frequency(50)
#setting the servo to move
servo.move(1, 125, 250)
