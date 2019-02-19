#Butt ton of imports
import spidev
import Adafruit_PCA9685
import CONSTANTS

class motor:

    pwm = Adafruit_PCA9685.PCA9685()

    #Functions for darned near everything
    def accelerate(self, motor1 = False, motor2 = False, speed1 = False, speed2 = False):

        for i in range(SERVOMAX):

            if motor2 is True:




            else:

                #Slowly accelerates the motors to full speed
                pwm.set_pwm(0, i, 0)
                pwm.set_pwm(15, -i, 0)

    def deccelerate(self, motor1 = False, motor2 = False):

    def turnLeft(self, hardness = 0):

    def turnRight(self, hardness = 0):

    def stop(self, motor1 = False, motor2 = False):

        if motor1 and motor2 is True:

            pwm.set_all_pwm(0, 0)

        elif motor1 is True and motor2 is False:

            pwm.set_pwm(0, 0, 0)

        elif motor1 is False and motor2 is True:

            pwm.set_pwm(15, 0, 0)

        else:

            pwm.set_all_pwm(0, 0)

    def reverse(self):

        motor.stop()
        motor.deccelerate()


def pingSenseHat():

def pingUltra():

def playMusic(file):

def readChannel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data