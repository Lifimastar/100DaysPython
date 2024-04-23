# Turtle Graphics, Tuples and Importing Modules

# Python Turtle

from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(100)

# Graphical user interfaces
tim = Turtle()

for _ in range(4):
    tim.forward(100)
    tim.left(90)


screen = Screen()
screen.exitonclick()

