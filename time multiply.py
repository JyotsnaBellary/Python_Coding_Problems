class Time:
    pass

def read(t):
    t.hour = float(input("Enter hours:"))
    t.minute = float(input("Enter minutes:"))
    t.second = float(input("Enter seconds:"))

def multiply(t1, n):
    t1.hour = t1.hour * n
    t1.minute = t1.minute * n
    t1.second = t1.second * n

    if t1.second >= 60:
        t1.second -= 60
        t1.minute += 1

    if t1.minute >= 60:
        t1.minute -= 60
        t1.hour += 1
        

    print("The duration is %g:%g:%g" %(t1.hour, t1.minute, t1.second))
time1 = Time()
read(time1)
n = int(input("Enter number:"))

multiply(time1,n)
