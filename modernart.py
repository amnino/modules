from turtle import *
from random import randint

def rectangle():
  randomcolor()
  randomposition()
  length = randint(0,50)
  bredth = randint(2,60)
  begin_fill()
  forward(length)
  right(90)
  forward(bredth)
  right(90)
  forward(length)
  right(90)
  forward(bredth)
  end_fill()
  
  
def ranstar():
  randomcolor()
  randomposition()
  dim = randint(4,60)
  begin_fill()
  for i in range(5):
    forward(dim)
    right(144)
  end_fill()

def circledrw():
  randomcolor()
  randomposition()
  x = randint(0,67)
  dot(x)

def randomcolor():
  red = randint(0,255)
  blue = randint(0,255)
  green = randint(0, 255)
  color(red, blue, green)
  
def randomposition():
  penup()
  x = randint(-100, 100)
  y = randint(-100,100)
  goto(x,y)
  pendown()

def randomhead():
  turn = randint(1,360)
  setheading(turn)
  
shape('turtle')
hideturtle()
speed(0)
for i in range(40):
  randomcolor()
  randomhead()
  randomposition()
  stamp()
clear()
setheading(0)
for i in range(30):
  rectangle()
clear()
for i in range(40):
  circledrw()
clear()
for i in range(30):
  ranstar()
