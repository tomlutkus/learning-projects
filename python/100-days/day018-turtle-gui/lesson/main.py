# from turtle import Turtle, Screen
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("black", "red")
for _ in range(4):
    tim.forward(100)
    tim.right(90)


my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
