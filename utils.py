#Butt ton of imports
import spidev
import  time
import Adafruit_PCA9685
import CONSTANTS as c

class Motor:

    currentSpeed = 0
    currentDir = None
    obsForward = None
    obsBehind = None
    obsLeft = None
    obsRight = None
    pwm = Adafruit_PCA9685.PCA9685()

    #Function to accelerate forward
    def accelerate(self, motor1 = False, motor2 = False, speed1 = c.SERVOMAX, speed2 =c.SERVOMAX):

        if motor1 is True and motor2 is True and speed2 is False:

            for (Motor.currentSpeed) in range(speed1):

                Motor.set_pwm(0, Motor.currentSpeed, 0)
                Motor.set_pwm(15, -Motor.currentSpeed, 0)

        elif motor1 is True and motor2 is True and speed2 is not False:

            if abs(Motor.currentSpeed - speed1) > abs(Motor.currentSpeed - speed2):

                tempMax = speed1

            else:

                tempMax = speed2

            for (Motor.currentSpeed) in range(tempMax):

                Motor.set_pwm(0, speed1, 0)
                Motor.set_pwm(15,speed2, 0)

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

    #Function to turn the car right
    def turnRight(self, hardness = 0):

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
        Motor.deccelerate()

    #Begin going straight forward
    def start(self):

        Motor.stop()
        time.sleep(.5)
        Motor.accelerate()


def pingSenseHat():

def pingUltra():

def playMusic(file):

def readChannel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data