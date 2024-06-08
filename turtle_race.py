from turtle import *
from random import randint

speed("fastest")  # Slow down the drawing speed for better visibility
penup()
goto(-100, 150)
for setup in range(9):
    write(setup)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(30)

red = Turtle()
red.color("red")
red.shape('turtle')
red.penup()
red.goto(-160, 140)

green = Turtle()
green.color("green")
green.shape('turtle')
green.penup()
green.goto(-160, 100)

blue = Turtle()
blue.color("blue")
blue.shape('turtle')
blue.penup()
blue.goto(-160, 60)

yellow = Turtle()
yellow.color("orange")
yellow.shape('turtle')
yellow.penup()
yellow.goto(-160, 20)

# Reset the positions of the turtles for the race
red.goto(-160, 140)
green.goto(-160, 100)
blue.goto(-160, 60)
yellow.goto(-160, 20)

for turn in range(100):
    red.forward(randint(1, 5))
    green.forward(randint(1, 5))
    blue.forward(randint(1, 5))
    yellow.forward(randint(1, 5))

done()  # Finish the drawing when done
