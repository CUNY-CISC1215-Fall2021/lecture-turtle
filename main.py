import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, size, angle):
    for i in range(n):
        t.forward(size)
        t.left(angle)

def polygon(t, n, size):
    angle = 360 / n
    polyline(t, n, size, angle)

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

    polyline(t, n, step_length, step_angle)



arc(bob, 80, 45)

turtle.mainloop()