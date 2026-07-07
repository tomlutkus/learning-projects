import turtle as t
import tkinter

screen = t.Screen()
screen.setup(width=600, height=600)

tim = t.Turtle()
tim.shape("turtle")
tim.color("black", "red")
tim.pensize(5)

for _ in range(10):
    tim.forward(20)
    tim.pu()
    tim.forward(20)
    tim.pd()

print(screen.canvheight)
screen.exitonclick()