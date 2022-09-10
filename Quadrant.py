import math

class point:
    """which quadrant does it belong to?"""
def check(po):
    if po.x == 0 and po.y == 0:
        print("Point is on origin")
    if po.x < 0:
        if po.y < 0:
            print("3rd Quadrant")
        else:
            print("4th Quadrant")
    else:
        if po.y < 0:
            print("2nd Quadrant")
        else:
            print("1st Quadrant")
        

p = point()
p.x = float(input("enter x coordinate:"))
p.y = float(input("enter y coordinate:"))
check(p)
