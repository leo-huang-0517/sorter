from pybricks.pupdevices import ColorDistanceSensor, Motor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait

# We'll use a dial
dial = Motor(Port.A)
# First, we'll move the dial to zero.
dial.run_target(500, 0, Stop.COAST)

# Initialize the sensor.
sensor = ColorDistanceSensor(Port.C)

while True:
    # Read the color.
    color = sensor.color()
    # Print the measured color.
    print(color)
    
    if color==Color.RED:
        dial.run_target(500, 0)
    elif color==Color.BLUE:
        dial.run_target(500, 90)
    # Move the sensor around and see how
    # well you can detect colors.
    # Wait so we can read the value.
    wait(1000)
