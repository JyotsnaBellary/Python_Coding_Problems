import math

def div(a,b):
    x, y = divmod(a,b)
    return x,y

a = float(input("Enter A:"))
b = float(input("Enter B:"))
q, r = div(a,b)
print("Reminder =",r)
print("quotient =",q)
