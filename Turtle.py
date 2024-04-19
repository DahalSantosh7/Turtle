import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Colorful Spiral Pattern")
screen.bgcolor("black")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Function to generate a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Draw colorful spiral
for i in range(150):
    t.color(random_color())
    t.forward(200)
    t.left(121)

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()