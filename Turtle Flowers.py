#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Melissa
#
# Created:     20/07/2015
# Copyright:   (c) Melissa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
numberOfSteps = int(input('Pick a number between 1 and 25.'))
for steps in range(numberOfSteps):
    turtle.color('black')
    turtle.forward(50)
    turtle.right(45)
    for steps in range(8):
        turtle.color('red')
        turtle.forward(25)
        turtle.left(45)
        for steps in range(3):
            turtle.color('purple')
            turtle.forward(20)
            turtle.right(120)



