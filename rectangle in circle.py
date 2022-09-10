import math

class rectangle:
    """rectangle"""
class circle:
    """circle"""
class point:
    """point"""
def read(a):
    a.x = float(input("Enter x coordinate of center"))
    a.y = float(input("Enter y coordinate of center"))
    
def corners(r):
    r.point2 = point()
    r.point2.x = r.point1.x + r.width
    r.point2.y = r.point1.y + r.length

def distance(c,r):
    d1 =math.sqrt((c.center.x-r.point1.x)**2+(c.center.y-r.point1.y)**2)
    d2 =math.sqrt((c.center.x-r.point2.x)**2+(c.center.y-r.point2.y)**2)

    rectincircle(c,r,d1,d2)
    
def rectincircle(c,r,d1,d2):
    if d1 == c.radius and d2 == c.radius:
        print("Rectangle lies on the circle")
    elif (d1 < c.radius and d2 < c.radius) or (d1 < c.radius and d2 == c.radius) or (d1 == c.radius and d2 < c.radius):
        print("Rectangle lies inside the circle")
    else:
        print("Rectangle lies outside the circle")

print("Enter the attributes of the circle:")
c = circle()
c.radius = float(input("Enter radius"))
c.center = point()
print("Enter coordinates of the center:")
read(c.center)

print("Enter the attributes of the rectangle:")
rect = rectangle()
rect.length = float(input("Enter length"))
rect.width = float(input("Enter width"))
rect.point1 = point()
print("Enter coordinates of the corner:")
read(rect.point1)

corners(rect)
distance(c,rect)
