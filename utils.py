#Butt ton of imports
import spidev

#Functions for darned near everything
def accelerate(motor1, motor2 = False):

def deccelerate(motor1, motor2 = False):

def turnLeft():

def turnRight():

def stop():

def reverse():

def pingSenseHat():

def pingUltra():

def playMusic(file):

def readChannel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data