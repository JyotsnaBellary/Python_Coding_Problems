class complex:
    """complex"""
def add(c):
    c.r = c.r1 + c.r2
    c.i = c.i1 + c.i2
    if c.i > 0:
        print("The sum of the complex numbers is: %g + %gi"%(c.r,c.i))
    else:
        print("The sum of the complex numbers is: %g - %gi"%(c.r,c.i))
        
def subtract(c):
    c.r = c.r1 - c.r2
    c.i = c.i1 - c.i2
    if c.i > 0:
        print("The difference of the complex numbers is: %g + %gi"%(c.r,c.i))
    else:
        print("The difference of the complex numbers is: %g - %gi"%(c.r,c.i))
    
def multiply(c):
    c.r = (c.r1*c.r2)-(c.i1*c.i2)
    c.i=(c.r1*c.i2)+(c.i1*c.r2)
    if c.i > 0:
        print("The multiplication of the complex numbers is: %g + %gi"%(c.r,c.i))
    else:
        print("The multiplication of the complex numbers is: %g - %gi"%(c.r,c.i))
    
c = complex()   
print("Enter the first number:")
c.r1 = float(input("Enter the real part:"))
c.i1 = float(input("Enter the imaginary part:"))
print("Enter the second number:")
c.r2 = float(input("Enter the real part:"))
c.i2 = float(input("Enter the imaginary part:"))
add(c)
subtract(c)
multiply(c)

"""class complex:
    """represent"""
def read(num):
    num.a=int(input("enter a real part:"))
    num.b=int(input("enetr the imaginary part:"))
def add(num1,num2):
    add=complex()
    add.a=num1.a+num2.a
    add.b=num1.b+num2.b
    return add

def sub(num1,num2):
    sub=complex()
    sub.a=num1.a-num2.a
    sub.b=num1.b-num2.b
    return sub
    
def mul(num1,num2):
    mul=complex()
    mul.a=(num1.a*num2.a)-(num1.b*num2.b)
    mul.b=(num1.a*num2.b)+(num1.b*num2.a)
    return mul
    def print_complex(num):
    if(num.b>0):
        print("%g+%gi"%(num.a,num.b))
    elif(num.b<0):
        print("%g%gi"%(num.a,num.b))
    else:
        print("%g"%(num.a))

num1=complex()
print("Enter the first complex no:")
read(num1)

num2=complex()
print("Enter the second complex no:")
read(num2)

add_res=add(num1,num2);
print("Sum=",end="")
print_complex(add_res)

sub_res=sub(num1,num2);
print("Difference=",end="")
print_complex(sub_res)

mul_res=mul(num1,num2);
print("Product=",end="")
print_complex(mul_res)"""





