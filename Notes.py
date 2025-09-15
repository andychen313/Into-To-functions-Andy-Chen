import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)
def doubleSquare():
    y = 100
    for i in range(2):
        square(y)
        y = y*2
doubleSquare()

turtle.done()

 # Strings represent characters or text
x = "Dang it yi"
#inputs output strings
name = input("What's your name")
print(name)
def add(x, y):
    return x + y 
z = add(5, 15)
print(z) 

 #integers or numbers
a = int('5')
bill = input("How much was the bill?")
print(int(bill) * .15)

name = "Mason"

#use F string
print(f"His name is (name)")