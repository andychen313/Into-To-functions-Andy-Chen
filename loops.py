import turtle
from turtle import *
t = Turtle()


def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5)



""" def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)
square(200)


def addSquares(iRange):
    length = 200
    for i in range(iRange):
        square(200)
        length = length +20
        t.left(5)
addSquares(60) 


def star(x):
    for i in range(5):
        t.forward(x)
        t.left(144)
star(200)


def many_stars():
    length = 200
    for i in range(60):
        star(length)
        t.left(10)
        length = length +20
many_stars()


def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)
square(200)


def addSquares(iRange):
    length = 200
    for i in range(60):
        square(length)
        length = length
        t.left(5)
addSquares(60) """


turtle.done()