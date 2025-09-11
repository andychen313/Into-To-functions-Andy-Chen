import turtle
from turtle import *
t = Turtle()
t.speed('fastest')


""" sidelength = 100
rotate = 90
def square(x, y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100, 90)


def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5) """



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


""" def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)


def spiral():
    length = 5
    for i in range(60):
        square(length)
        t.right(5)
        length +=5
spiral() """

""" def star(size):
    for i in range(5):
        t.forward(size)
        t.right(144)


def star_spiral():
    size = 5
    for i in range(60):
        star(size)
        t.right(5)
        size +=5
star_spiral() """


def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)


def spiral():
    length = 80
    right = 10
    for i in range(150):
        square(length)
        length =+80
        t.right(20)
        right +=100
spiral()





turtle.done()