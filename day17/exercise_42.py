# More Turtle Graphics, Event Listeners, State and Multiple Instances

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()

# Functions as inputs

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

print(calculator(2, 3, add))

# Higher Order Functions

