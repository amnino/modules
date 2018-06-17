#!/bin/python3
from random import randint
from turtle import *
speed(20)
penup()

goto(-140,140)
for step in range(1,15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

blue = Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-160,100)
for n in range(36):
  blue.right(10)
blue.pendown()

red = Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-160,70)
for n in range(36):
  red.right(10)
red.pendown()

green = Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-160,40)
for n in range(36):
  green.right(10)
green.pendown()

yellow = Turtle()
yellow.color('yellow')
yellow.shape('turtle')
yellow.penup()
yellow.goto(-160,10)
for n in range(36):
  yellow.right(10)
yellow.pendown()

for i in range(100):
    blue.forward(randint(1,5))
    red.forward(randint(1,5))
    green.forward(randint(1,5))
    yellow.forward(randint(1,5))
