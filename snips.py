#!/bin/python3

import turtle
from random import choice, randint

elsa = turtle.Turtle()

# elsa.color("cyan")

# turtle.Screen().bgcolor("pink")

colours = ['yellow', ' gold', ' orange', ' red', ' maroon', ' violet', ' magenta', ' purple', ' navy', ' blue', ' skyblue', ' cyan', ' turquoise', ' lightgreen', ' green', ' darkgreen', ' chocolate', ' brown', ' black', ' gray', ' white']



#   PRETTTTY
for i in range(12):
  # elsa.color(choice(colours))
  r,g,b = randint(0,255), randint(0,255), randint(0,255)
  elsa.color(r,g,b)
  # turtle.Screen().bgcolor(choice(colours))
  turtle.Screen().bgcolor(b,g,r)
  for j in range(2):
    elsa.forward(100)
    elsa.right(60)
    elsa.forward(100)
    elsa.right(120)
  elsa.right(30)
  
  
# def branch():
#   for i in range(3):
#     for i in range(3):
#         elsa.forward(30)
#         elsa.backward(30)
#         elsa.right(45)
#     elsa.left(90)
#     elsa.backward(30)
#     elsa.left(45)
#   elsa.right(90)
#   elsa.forward(90)    
  

# for i in range(8):
#     branch()
#     elsa.left(45)




# ---------------------------------------------------

# #!/bin/python3

# from turtle import *

import turtle
from random import randint

turtle.shape("turtle")
turtle.speed(5)

def random_colour():
  r,g,b = randint(0,255), randint(0,255), randint(0,255)
  turtle.color(r,g,b)

def random_place():
  turtle.penup()
  x = randint(-100,100)
  y = randint(-100,100)
  turtle.goto(x,y)
  turtle.pendown()
  
  
def random_heading():
  turtle.setheading(randint(1,360))
  
for i in range(10):
  random_colour()
  random_heading()
  random_place()
  turtle.stamp()
  
  
turtle.clear()




## RANDOM TURTLES ON CANVAS 
# #!/bin/python3

# from turtle import *

import turtle
from random import randint

turtle.shape("turtle")
turtle.speed(5)

def random_colour():
  r,g,b = randint(0,255), randint(0,255), randint(0,255)
  turtle.color(r,g,b)

def random_place():
  turtle.penup()
  x = randint(-100,100)
  y = randint(-100,100)
  turtle.goto(x,y)
  turtle.pendown()
  
  
def random_heading():
  turtle.setheading(randint(1,360))
  
for i in range(10):
  random_colour()
  random_heading()
  random_place()
  turtle.stamp()
  
  
# turtle.clear()
