import turtle
import math

bob = turtle.Turtle()

def polygon(t, n, size):
    angle = 360 / n
    for i in range(n):
        t.forward(size)
        t.left(angle)

def square(t, size):
    polygon(t, 4, size)

def circle(t, radius):
    circumference = radius * 2 * math.pi
    polygon(bob, 50, circumference / 50)

circle(bob, 80)

turtle.mainloop()