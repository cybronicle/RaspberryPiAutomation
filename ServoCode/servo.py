#!/usr/bin/env python
from ServoPi import PWM
from ServoPi import Servo

class servoDriver(object):
    def __init__(self):
	#creating objects for the PWM and Motor
        self.pwm = pulseWidthModulation()
        self.ServoMotor = motor()

    def pulseWidthModulation(self):
        #Pulse Width Modulation(PWM) instatiation
        self.pwm = PWM(0x40)
        #Sets the PWM to a frequency of 200 Hz
        self.pwm.set_pwm_freq(200)
        #Alloww the output to be displayed
        self.pwm.output_enable()
        #Setting the channel for data stream to 1, time period to 1024 out of 4095.
        self.pwm.set_pwm(1,0,1024)

    def motor(self):
        #Instantiation of the servo object
        servo = Servo(0x40)
        #setting frequency for the PWM to interact with the PWM object
        servo.set_frequency(50)
        #setting the servo to move
        servo.move(1, 125, 250)

class RCServo(object):
    def __init__(self):
        self.RC_driver = servoDriver()

if name == "main":
    RC =  RCServo()
