class point:
    """Collinear"""
def read(p):
    p.x = float(input("Enter x coordinate"))
    p.y = float(input("Enter y coordinate"))    

def calculate(p1,p2,p3):
    a = p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
    if a == 0:
        print("Yes")
    else:
        print("No")
p1 = point()
p2 = point()
p3 = point()
print("Enter coordinates of first point:")
read(p1)
print("Enter coordinates of second point:")
read(p2)
print("Enter coordinates of third point:")
read(p3)

print("Are the points collinear?")
calculate(p1,p2,p3)

