import math

class circle:
    """length"""
def read(c):
    c.radius = float(input("Enter the radius"))
    c.angle = float(input("Enter the angle"))
def arclength(c):
    if c.angle > 360.0:
        print("Arc not possible")
        return
    pi = 22/7
    arc_length = (pi*2*c.radius) * (c.angle/360)
    print("Arc Length is", arc_length)

c1 = circle()
print("Enter radius and angle")
read(c1)
arclength(c1)
