#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Melissa
#
# Created:     19/07/2015
# Copyright:   (c) Melissa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#import turtle
#turtle.color('blue')
#turtle.forward(100)
#turtle.left(120)
#turtle.color('green')
#turtle.forward(100)
#turtle.left(120)
#turtle.color('red')
#turtle.forward(100)
import turtle
#for step in range(3):
#    turtle.forward(300)
#    turtle.right(120)
nbrsides = 15
for steps in range(nbrsides):
    turtle.forward(50)
    turtle.left(360/nbrsides)
    for steps in range (3):
        turtle.color('blue')
        turtle.forward(50)
        turtle.left(120)


