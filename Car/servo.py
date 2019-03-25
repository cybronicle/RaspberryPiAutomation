#!/usr/bin/env python
from ServoPi import PWM
from ServoPi import Servo

#use __init__ function to pass the pin values when recieved for each servo instance
PIN_left = 0
PIN_right = 1

class servoDriver(object):
    servoFrequencyValue = 50
    PWMFrequencyValue = 200

    def __init__(self):
	#creating objects for the PWM and Motor
        self.pwm = pulseWidthModulation()
        self.ServoMotor = motor()

    def pulseWidthModulation(self):
        #Pulse Width Modulation(PWM) instatiation
        self.pwm = PWM(0x40)
        #Sets the PWM to a frequency of 200 Hz
        self.pwm.set_pwm_freq(self.PWMFrequencyValue)
        #Allow the output to be displayed
        self.pwm.output_enable()
        #Setting the channel for data stream to 1, time period to 1024 out of 4095.
        self.pwm.set_pwm(1,0,1024)

    def motor(self):
        #Instantiation of the servo object
        self.servo = Servo(0x40)
        #setting frequency for the PWM to interact with the PWM object
        self.servo.set_frequency(self.frequencyValuse)
        #setting the servo to move
        self.servo.move(1, 125, 250)

    def set_PWM_frequency(self, value):
        self.PWMFrequencyValue = value
        self.pwm.set_pwm_freq(self.PWMFrequencyValue)

    def get_PWM_frequency(self):
        return self.PWMFrequencyValue

    def set_servo_frequency(self, value):
        self.servoFrequencyValue = value
        self.servo.set_frequency(self.servoFrequencyValue)

    def get_servo_frequency(self):
        return self.servoFrequencyValue

class RCServo(object):
    def __init__(self):
        self.Right_RC_driver = servoDriver()
        self.Left_RC_driver = servoDriver()
if name == "main":
    RC =  RCServo()
