from turtle import *

screen = Screen()
screen.setup(400,400)
screen.bgcolor('#A7E30E')
style=('Arial', 40, 'bold')
write ('Hello', font = style, align = 'center')
hideturtle()
penup()
right(90)
forward(60)
write('World!!', font = style, align='center')
setposition(0.0,0.0)
dot(300, 'grey')
backward(70)
style2=('Arial', 20, 'bold')
write('Hey!', font = style2,align = 'center')
forward(70)
style3=('Arial', 40, 'bold')
write('Aman G', font = style3, align = 'center')
