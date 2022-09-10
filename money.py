n = int(input())
m = int(input())
N = []
M = []

if n>0 and n<=1000 and m>0 and m<=1000:
    for i in range(n):
        a = int(input())
        N.append(a)
    
    for i in range(m):
        a = int(input())
        M.append(a)
        
    su = []
    
    for i in N:
        for j in M: 
            s = i * j
            su.append(s)
    
    count = 0
    for i in su:
        if i % 2 == 0:
            count = count + 1
    
    print(count)
