#!/usr/bin/python3

import utils as u
from multiprocessing import Process, Queue, Pipe
import cv2
from oracle import oracling


def motor():
    currentState = 0

    # Set up the motor object
    car = u.Motor()
    car.build()

    # Set up the OpenCV Process with pipe
    parent_conn, child_conn = Pipe()
    p = Process(target=oracling, args=(child_conn,))
    p.start()

    # What the different states mean
    states = ["Full Speed", "0 left", "1 left", "2 left", "3 left", "4 left", "0 right", "1 right", "2 right",
              "3 right",
              "4 right"]

    car.start()

    while True:
        val = parent_conn.recv()

        # Decide the next state
        if (val == 0):
            currentState = val
            car.setSpeed(motor1=True, motor2=True)
            print('Val = 0, right speed is %f, car left speed is %f' % (car.currentRight, car.currentLeft))

        elif (0 < val <= 5):
            currentState = val - 1
            car.turnLeft(hardness=currentState)
            print('Val = %d, right speed is %f, car left speed is %f' % (val, car.currentRight, car.currentLeft))

        elif ((6 <= val <= 10)):
            currentState = val
            car.turnRight(hardness=val - 6)
            print('Val = %d right speed is %f, car left speed is %f' % (val, car.currentRight, car.currentLeft))

        elif (val == 13):
            currentState = 13
            car.stop()
            print('Val = %d, right speed is %f, car left speed is %f' % (val, car.currentRight, car.currentLeft))
            p.close()

        else:
            currentState = 11
            car.stop()
            print('Val = %d, right speed is %f, car left speed is %f' % (val, car.currentRight, car.currentLeft))

motor()
