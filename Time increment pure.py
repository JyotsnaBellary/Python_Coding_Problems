class Time:
    pass

def read(t):
    t.hour = float(input("Enter hours:"))
    t.minute = float(input("Enter minutes:"))
    t.second = float(input("Enter seconds:"))
        
    
def increment(time,seconds):
    time2.second = time.second + seconds

    if time2.second >= 60:
        time2.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

time = Time()
read(time)
time2 = Time()
seconds = float(input("Enter incrementing seconds:"))
increment(time,seconds)

print("%d:%d:%d" %(time.hour, time.minute, time2.second))
