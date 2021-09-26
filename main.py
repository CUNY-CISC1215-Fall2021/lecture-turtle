import turtle

bob = turtle.Turtle()

def polygon(t, n, size):
    angle = 360 / n
    for i in range(n):
        t.forward(size)
        t.left(angle)

def square(t, size):
    polygon(t, 4, size)

square(bob, 100)

turtle.mainloop()