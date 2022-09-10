import math

class point:
    """for point"""
class rectangle:
    """for rectangle"""

def read_corner(box):
    box.p1 = point()
    box.p1.x = float(input("Enter x coordinate:")) 
    box.p1.y = float(input("Enter y coordinate:"))

def new_corner(box, dx, dy):
    box.p1.x += dx
    box.p1.y += dy
    print("New location of rectangle: (", box.p1.x, ",", box.p1.y, ")")

box = rectangle()
print("Enter corner of rectangle:")
read_corner(box)
dx = float(input("Enter width by how much rectangle should move:"))
dy = float(input("Enter length by how much rectangle should move:"))
new_corner(box,dx,dy)
