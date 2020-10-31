from turtle import *

screen = Screen()

turtles = []
t = 10

for x in range(t):
    turtle = Turtle()
    r = (360/t) * x
    turtle.right(r)
    turtles.append(turtle)

for turtle in turtles:
    turtle.forward(100)
    turtle.left(10)
    turtle.back(20)
    turtle.left(10)
    turtle.forward(40)

screen.exitonclick()