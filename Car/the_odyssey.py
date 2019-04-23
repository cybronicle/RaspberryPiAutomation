import utils as u
import multiprocessing

# Set up the motor object
car = u.Motor()

# start openCV
CV = multiprocessing.Process(name='oracle', target='/oracle.py')

# connect to site if we have time

# 0 means full speed ahead
states = ["Full Speed", "0 left", "1 left", "2 left", "3 left", "4 left", "0 right", "1 right", "2 right", "3 right",
          "4 right"]
state = 0

car.start()
CV.start()

while True:

    # Ping openCV to set the state
    try:

        state = True

    except:

        pass

    # Decide the next state
    if state == 0:

        car.normalize()

    if 0 < state <= 5:

        car.turnLeft(state - 1)

    if 6 <= state <= 10:

        car.turnRight(state - 6)

    else:

        car.stop()

    # Send video stream to site
