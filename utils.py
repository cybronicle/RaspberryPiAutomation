# Butt ton of imports
import time
from adafruit_servokit import ServoKit
import CONSTANTS as c

class Motor:
    def build(self):
        self.kit = ServoKit(channels=16)
        self.currentRight = 0
        self.currentLeft = 0
        self.currentDir = None
        self.obsForward = None
        self.obsBehind = None
        self.obsLeft = None
        self.obsRight = None

    # Function to set the speed
    def setSpeed(self, motor1=False, motor2=False, speed1=c.SERVOMAX, speed2=c.SERVOMAX):

        if motor1 is True and motor2 is False:

            self.kit.continuous_servo[c.RIGHT].throttle = -.5

        elif motor1 is False and motor2 is True:

            self.kit.continuous_servo[c.LEFT].throttle = speed2

        else:

            self.kit.continuous_servo[c.RIGHT].throttle = -speed1
            self.kit.continuous_servo[c.LEFT].throttle = speed2

        self.currentRight = speed1
        self.currentLeft = speed2

    # Function to turn the car right
    def turnRight(self, hardness=0):

        if hardness == 0:

            self.setSpeed(motor1=True, motor2=True, speed1=0.66, speed2=1.0)

        elif hardness == 1:

            self.setSpeed(motor1=True, motor2=True, speed1=0.33, speed2=1.0)

        elif hardness == 2:

            self.setSpeed(motor1=True, motor2=True, speed1=0.0, speed2=1.0)

        elif hardness == 3:

            self.setSpeed(motor1=True, motor2=True, speed1=-0.33, speed2=1.0)

        elif hardness == 4:

            self.setSpeed(motor1=True, motor2=True, speed1=-0.66, speed2=1.0)

        else:

            self.setSpeed(motor1=True, motor2=True, speed1=0.66, speed2=1.0)

    # Function to turn the car left
    def turnLeft(self, hardness=0):

        if hardness == 0:

            self.setSpeed(motor1=True, motor2=True, speed1=1.0, speed2=0.66)

        elif hardness == 1:

            self.setSpeed(motor1=True, motor2=True, speed1=1.0, speed2=0.33)

        elif hardness == 2:

            self.setSpeed(motor1=True, motor2=True, speed1=1.0, speed2=0.0)

        elif hardness == 3:

            self.setSpeed(motor1=True, motor2=True, speed1=1.0, speed2=-0.33)

        elif hardness == 4:

            self.setSpeed(motor1=True, motor2=True, speed1=1.0, speed2=-0.66)

        else:

            self.setSpeed(motor1=True, motor2=True, speed1=1.0, speed2=0.66)

    # Function to stop a motor
    def stop(self, motor1=False, motor2=False):

        if motor1 and motor2 is True:

            self.setSpeed(motor1=True, motor2=True, speed1=c.SERVOMIN, speed2=c.SERVOMIN)

        elif motor1 is True and motor2 is False:

            self.setSpeed(motor1=True, speed1=c.SERVOMIN)

        elif motor1 is False and motor2 is True:

            self.setSpeed(motor2=True, speed2=c.SERVOMIN)

        else:

            self.setSpeed(motor1=True, motor2=True, speed1=c.SERVOMIN, speed2=c.SERVOMIN)

    # Begin going straight back
    def reverse(self):
        self.stop()
        time.sleep(.01)
        self.setSpeed(motor1=True, motor2=True, speed1=-c.SERVOMAX, speed2=-c.SERVOMAX)

    # Begin going straight forward
    def start(self):

        self.setSpeed(motor1=True, motor2=True)

    # Set each motor to the same speed
    def normalize(self):

        if self.currentLeft > self.currentRight:

            self.setSpeed(motor1=True, speed1=self.currentRight)

        elif self.currentLeft < self.currentRight:

            self.setSpeed(motor2=True, speed2=self.currentLeft)

        else:

            pass

    def kill(self):
        self.kit.continuous_servo[c.RIGHT].throttle = -0.002
        self.kit.continuous_servo[c.LEFT].throttle = -0.002
