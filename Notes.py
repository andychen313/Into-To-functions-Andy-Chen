""" import turtle
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
print(f"His name is (name)") """

""" #Float
bill = 3.14

students = ["Cadee", "Mason", "Andy"]
#Can reference each item by their index
print(students[0]) #Prints Cadee

# add student
students.append("Alina")

#We can iterate or loop through a list
for student in students:
    print(student) """


""" #Boolean true or false
x = True
y = False
#evaluations use double ==
if y == True:
    print("hello Rodney")
else:
    print("Goodbye Rodney") """

""" #Evaluations in lists
students = ["Cadee", "Mason", "Andy"]
if "Alina" in students:
    print("She's here")
else:
    students.apprehend("Alina")
    print("We added Alina") """

""" x = 91
if x < 10:
    print("Less")
elif x == 10:
    print("Equal")
else:
    print("Greater than 10") """

""" students = ["Cadee", "Mason", "Andy", "Alina"]
for student in students:
    found = False
    if student == "Mason":
        print("Found Mason")
        found = True """

""" name = "Cadee"
print(name[0])
for letter in name:
    print(letter) """

""" students = ["Cadee", "Mason", "Andy"]
students.append("Alina")
for student in students:
    print(student) """

x = True
y = False
if y == True:
    print("Hello Rodney")
else:
    print("Goodbye Rodney")