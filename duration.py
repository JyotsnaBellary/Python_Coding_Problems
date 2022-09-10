class Time:
    pass

def read(t):
    t.hour = float(input("Enter hours:"))
    t.minute = float(input("Enter minutes:"))
    t.second = float(input("Enter seconds:"))

def subtract(t1,t2):
    th = t1.hour - t2.hour
    tm = t1.minute - t2.minute
    ts = t1.second - t2.second
    if th < 0:
        th *= -1
    if tm < 0:
        tm *= -1
    if ts < 0:
        ts *= -1
        

    print("The duration is %g:%g:%g" %(th, tm, ts))
time1 = Time()
read(time1)
time2 = Time()
read(time2)

subtract(time1, time2)
