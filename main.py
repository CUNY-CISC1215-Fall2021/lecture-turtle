import turtle
import math


def polyline(t, n, size, angle):
    """
    Draw the outline of a polygon.
    t: a Turtle object
    n: the number of sides to draw
    size: the length of each side of the polyline
    angle: the angle to turn between each side
    """
    for i in range(n):
        t.forward(size)
        t.left(angle)


def polygon(t, n, size):
    """
    Draw a closed polygon.
    t: a Turtle object
    n: the number of sides the polygon has
    size: the length of each size of the polygon
    """
    angle = 360 / n
    polyline(t, n, size, angle)


def square(t, size):
    """
    Draw a square.
    t: a Turtle object
    size: the length of each side of the square
    """
    polygon(t, 4, size)


def arc(t, radius, angle):
    """
    Draw an arc.
    t: a Turtle object
    radius: radius of the circle to draw around
    angle: the degrees of the circle to draw
    """
    circumference = radius * 2 * math.pi
    arc_length = circumference * angle / 360
    n = int(arc_length / 3) + 1

    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)


def circle(t, radius):
    """
    Draw a circle.
    t: a Turtle object
    radius: the radius of the circle
    """
    arc(t, radius, 360)


def petal(t, radius, angle):
    """
    Draw a flower petal.
    t: a Turtle object
    radius: the radius of the petal arc
    angle: the angle of the petal arc to draw
    """
    for i in range(2):
        arc(t, radius, angle)
        t.left(180 - angle)


def flower(t, n, radius, angle):
    """
    Draw a flower.
    t: a Turtle object
    n: the number of petals
    radius: the radius of the petal arc
    angle: the angle of the petal arc to draw
    """
    for i in range(n):
        petal(t, radius, angle)
        t.left(360 / n)


if __name__ == "__main__":
    bob = turtle.Turtle()

    flower(bob, 7, 100, 45)

    turtle.mainloop()
