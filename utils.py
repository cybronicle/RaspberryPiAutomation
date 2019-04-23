#Butt ton of imports
import time
from adafruit_servokit import ServoKit
import CONSTANTS as c

class Motor:

    kit = ServoKit(channels=16)

    currentSpeed = 0
    currentRight = 0
    currentLeft = 0
    currentDir = None
    obsForward = None
    obsBehind = None
    obsLeft = None
    obsRight = None

    #Function to set the speed)
    def setSpeed(self, motor1 = False, motor2 = False, speed1 = c.SERVOMAX, speed2 = c.SERVOMAX):

        if motor1 is True and motor2 is True:

            Motor.kit.continuous_servo[c.RIGHT].throttle = -speed1
            Motor.kit.continuous_servo[c.LEFT].throttle = speed2

        elif motor1 is True and motor2 is False:

            Motor.kit.continuous_servo[c.RIGHT].throttle = -speed1

        elif motor1 is False and motor2 is True:

            Motor.kit.continuous_servo[c.LEFT].throttle = speed2

        else:

            Motor.kit.continuous_servo[c.RIGHT].throttle = -speed1
            Motor.kit.continuous_servo[c.LEFT].throttle = speed2

        Motor.currentRight = speed1
        Motor.currentLeft = speed2

    #Function to turn the car left
    def turnRight(self, hardness = 0):

        if hardness == 0:

            self.setSpeed(motor1 = True, speed1 = self.currentLeft * 0.9)

        elif hardness == 1:

            self.setSpeed(motor1 = True, speed2 = self.currentLeft * 0.7)

        elif hardness == 2:

            self.setSpeed(motor1 = True, speed2 = self.currentLeft * 0.5)

        elif hardness == 3:

            self.setSpeed(motor1 = True, speed2 = self.currentLeft * 0.3)

        elif hardness == 4:

            self.setSpeed(motor1 = True, speed2 = self.currentLeft * 0.4)

        else:

            self.setSpeed(motor1 = True, speed2 = self.currentLeft * 0.9)

    #Function to turn the car right
    def turnLeft(self, hardness = 0):

        if hardness == 0:

            self.setSpeed(motor2 = True, speed1 = self.currentRight * 0.9)

        elif hardness == 1:

            self.setSpeed(motor2 = True, speed1 = self.currentRight * 0.7)

        elif hardness == 2:

            self.setSpeed(motor2 = True, speed1 = self.currentRight * 0.5)

        elif hardness == 3:

            self.setSpeed(motor2 = True, speed1 = self.currentRight * 0.3)

        elif hardness == 4:

            self.setSpeed(motor2 = True, speed1 = self.currentRight * 0.2)

        else:

            self.setSpeed(motor2 = True, speed1 = self.currentRight * 0.9)

    #Function to stop a motor
    def stop(self, motor1 = False, motor2 = False):

        if motor1 and motor2 is True:

            self.setSpeed(motor1 = True, motor2 = True, speed1 = c.SERVOMIN, speed2 = c.SERVOMIN)

        elif motor1 is True and motor2 is False:

            self.setSpeed(motor1 = True, speed1 = c.SERVOMIN)

        elif motor1 is False and motor2 is True:

            self.setSpeed(motor2 = True, speed2 = c.SERVOMIN)

        else:

            self.setSpeed(motor1 = True, motor2 = True, speed1 = c.SERVOMIN, speed2 = c.SERVOMIN)

    #Begin going straight back
    def reverse(self):

        self.stop()
        time.sleep(.01)
        self.setSpeed(motor1 = True, motor2 = True, speed1 = -c.SERVOMAX, speed2 = -c.SERVOMAX)

    #Begin going straight forward
    def start(self):

        self.setSpeed(motor1 = True, motor2 = True)

    #Set each motor to the same speed
    def normalize(self):

        if Motor.currentLeft > Motor.currentRight:

            self.setSpeed(motor1 = True, speed1 = Motor.currentRight)

        if Motor.currentLeft < Motor.currentRight:

            self.setSpeed(motor2 = True, speed2 = Motor.currentLeft)

        else:

            pass
