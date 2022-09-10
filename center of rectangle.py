import math

class point:
    """for point"""
class rectangle:
    """for rectangle"""
    
def read_lb(b):
    b.width = float(input("Enter width:"))
    b.length = float(input("Enter legth:"))
    
def read_corner(box):
    box.p1 = point()
    box.p1.x = float(input("Enter x coordinate:")) 
    box.p1.y = float(input("Enter y coordinate:"))
    
def center(box):
    box.p2 = point()
    box.p2.x = box.p1.x + box.width/2
    box.p2.y = box.p1.y + box.length/2
    print("(", box.p2.x, ",", box.p2.y, ")")
    
def resize(box, rwidth, rlength):
    box.width += rwidth
    box.length += rlength
    print("Updated width of recantangle:", box.width)
    print("Updated length of recantangle:", box.length)
    print("The new center is:")
    center(box)
    
box = rectangle()
print("Enter width and height of rectangle:")
read_lb(box)
print("Enter corner of rectangle:")
read_corner(box)
print("Center of the rectangle is:") 
center(box)
print("To resize the box:")
rwidth = float(input("Width should increase by: "))
rlength = float(input("Length should increase by: "))
resize(box, rwidth, rlength)


