#Butt ton of imports
import time
import Adafruit_PCA9685
import CONSTANTS as c

class Motor:

    currentSpeed = 0
    currentRight = 0
    currentLeft = 0
    currentDir = None
    obsForward = None
    obsBehind = None
    obsLeft = None
    obsRight = None
    pwm = Adafruit_PCA9685.PCA9685()

    #Function to accelerate forward (Basically just sets the speed
    def accelerate(self, motor1 = False, motor2 = False, speed1 = c.SERVOMAX, speed2 = -c.SERVOMAX):

        if motor1 is True and motor2 is True:

            Motor.set_pwm(0, speed1, 0)
            Motor.set_pwm(15, speed2, 0)

        elif motor1 is True and motor2 is False:

            Motor.set_pwm(0, speed1, 0)

        elif motor1 is False and motor2 is True:

            Motor.set_pwm(15, speed2, 0)

        else:

            for Motor.currentSpeed in range(c.SERVOMAX):

                Motor.set_pwm(0, speed1, 0)
                Motor.set_pwm(15, speed2, 0)

    #Function to slow down
    def deccelerate(self, motor1 = False, motor2 = False, speed1 = c.SERVOMIN, speed2 = c.SERVOMIN):

        if motor1 is True and motor2 is False:

            for i in range(Motor.currentSpeed):

                Motor.pwm.set_pwm(0, Motor.currentSpeed - i, 0)

        elif motor2 is True and motor1 is False:

            for i in range(Motor.currentSpeed):

                Motor.pwm.set_pwm(15, Motor.currentSpeed - i, 0)

        elif motor1 and motor2 is True:

            if abs(Motor.currentSpeed - speed1) < abs(Motor.currentSpeed - speed2):

                tempMin = speed1

            else:

                tempMin = speed2

            for i in range(tempMin):

                Motor.pwm.set_pwm(0, Motor.currentSpeed - i, 0)
                Motor.pwm.set_pwm(15, Motor.currentSpeed - i, 0)

        else:

            for i in range(c.SERVOMIN):

                Motor.pwm.set_pwm(0, Motor.currentSpeed - i, 0)
                Motor.pwm.set_pwm(15, Motor.currentSpeed - i, 0)

    #Function to turn the car left
    def turnLeft(self, hardness = 0):

        if hardness == 0:

            self.accelerate(motor2 = True, speed2 = self.currentRight * .2)

        elif hardness == 1:

            self.accelerate(motor2 = True, speed2 = self.currentRight * .4)

        elif hardness == 2:

            self.accelerate(motor2 = True, speed2 = self.currentRight * .6)

        elif hardness == 3:

            self.accelerate(motor2 = True, speed2 = self.currentRight * .8)

        elif hardness == 4:

            self.accelerate(motor2 = True, speed2 = self.currentRight * 1)

        else:

            self.accelerate(motor2 = True, speed2 = self.currentRight * .2)

    #Function to turn the car right
    def turnRight(self, hardness = 0):

        if hardness == 0:

            self.accelerate(motor1 = True, speed1 = self.currentLeft * .2)

        elif hardness == 1:

            self.accelerate(motor1 = True, speed1 = self.currentLeft * .4)

        elif hardness == 2:

            self.accelerate(motor1 = True, speed1 = self.currentLeft * .6)

        elif hardness == 3:

            self.accelerate(motor1 = True, speed1 = self.currentLeft * .8)

        elif hardness == 4:

            self.accelerate(motor1 = True, speed1 = self.currentLeft * 1)

        else:

            self.accelerate(motor1 = True, speed1 = self.currentLeft * .2)

    #Function to stop the car
    def stop(self, motor1 = False, motor2 = False):

        if motor1 and motor2 is True:

            Motor.pwm.set_all_pwm(0, 0)

        elif motor1 is True and motor2 is False:

            Motor.pwm.set_pwm(0, 0, 0)

        elif motor1 is False and motor2 is True:

            Motor.pwm.set_pwm(15, 0, 0)

        else:

            Motor.pwm.set_all_pwm(0, 0)

    #Begin going straight back
    def reverse(self):

        Motor.stop()
        time.sleep(.5)
        Motor.accelerate()

    #Begin going straight forward
    def start(self):

        for i in range(c.SERVOMAX/2):

            Motor.accelerate(motor1 = True, motor2 = True, speed1 = i, speed2 = i)

    #Set each motor to the same speed
    def normalize(self):

        if abs(Motor.currentLeft) > abs(Motor.currentRight):

            self.accelerate(motor1 = True, speed1 = Motor.currentRight)

        if abs(Motor.currentLeft) < abs(Motor.currentRight):

            self.accelerate(motor2 = True, speed2 = Motor.currentLeft)

        else:

            pass

def pingSenseHat():

    pass

def pingUltra():

    pass

def playMusic(file):

    pass
