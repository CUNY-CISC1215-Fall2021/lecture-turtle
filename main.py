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
    n = int(circumference / 3) + 1
    length = circumference / n
    
    polygon(bob, n, length)

def arc(t, radius, angle):
    circumference = radius * 2 * math.pi
    arc_length = circumference * angle / 360
    n = int(arc_length / 3) + 1

    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.forward(step_length)
        t.left(step_angle)

arc(bob, 200, 38)

turtle.mainloop()