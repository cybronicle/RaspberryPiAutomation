import utils as u
import oracle

# Set up the motor object
car = u.Motor()

# start openCV

# connect to site

# 0 means full speed ahead
states = ["Full Speed", "0 left", "1 left", "2 left", "3 left", "4 left", "0 right", "1 right", "2 right", "3 right",
          "4 right"]
state = 0

car.start()

while True:

    # Ping openCV

    # Decide the next state
    if state == 0:

        car.normalize()

    if state > 0 and state < 6:

        car.turnLeft(state - 1)

    if state > 5 and state < 11:

        car.turnRight(state - 6)

    else:

        car.stop()

    # Send video stream to site
