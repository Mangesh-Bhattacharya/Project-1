#######################################################################################
# Mangesh Bhattacharya
# Happy 75th Independence Day
# Date: 2022-08-15
#######################################################################################

import turtle  # Draw the Indian Flag

flag = turtle.Turtle()  # Create a turtle object
flag.speed(10)  # Set the speed of the turtle
flag.pensize(6)  # Set the width of the pen

# Draw the base of the flag
# Pull the pen up
# Move the turtle to the specified position
# Finally, pull the pen down


def move(a, b):
    flag.penup()
    flag.goto(a, b)
    flag.pendown()


# Set the color of the pen to blue
# Draw the base of the flag 24 times with a gap of 10 between each times
# Draw the base of the flag 95 pixels to the right
# Backward to the starting point of the flag by 95 pixels
# Rotate the turtle by 360/24 degrees = 15 degrees
# Move the turtle to the starting point of the flag by 95 pixels
# Draw the base of the flag 95 pixels and rotate it 360 degrees

flag.color("#0000FF")
for i in range(24):
    flag.forward(95)
    flag.backward(95)
    flag.left(15)
move(1, -95)
flag.circle(95, 360)

# Begin filling the shape with the color
# Set the color of the pen to green
# Move the turtle to the starting point of the flag by 99 pixels
# Draw the base of the flag 350 pixels
# Backward to the starting point of the flag by 700 pixels
# Rotate the turtle by 90 degrees to the right
# Draw the base of the flag 350 pixels
# End filling the shape with the color

flag.begin_fill()
flag.color("#008000")
move(0, -99)
flag.forward(350)
flag.backward(700)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.end_fill()

# Set the color of the pen to orange
# Move the turtle to the starting point of the flag -200 pixels and 100 pixels down
# Follow the same pattern as above or follow whichever pattern you prefer
# End filling the shape with the color

flag.color("#FF8C00")
move(-200, 100)
flag.begin_fill()
flag.forward(150)
flag.backward(700)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.end_fill()

# Finish the drawing of the flag

turtle.done()
