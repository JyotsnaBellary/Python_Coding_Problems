import math

class circle:
    """circle"""
class point:
    """point"""

def read(a):
    a.x = float(input("Enter x coordinate of center"))
    a.y = float(input("Enter y coordinate of center"))
    
def distance(c):
    d=math.sqrt((c.center.x-c.point1.x)**2+(c.center.y-c.point1.y)**2)
    print("Distance between the points is:", d)
    return d

def pointincircle(distance, c):
    if distance == c.r:
        print("The point is lying on the circle.")
    elif distance < c.r:
        print("The point is lying inside the circle")
    else:
        print("Point is lying outside the circle")
c = circle()
c.r = float(input("Enter radius"))

c.center = point()
print("Enter coordinates of the center:")
read(c.center)

c.point1 = point()
print("Enter coordinates of point:")
read(c.point1)

dist = distance(c)
pointincircle(dist, c)
