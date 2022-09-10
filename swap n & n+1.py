ls=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    w=input("enter the elements:")
    ls.append(w)

if n % 2 != 0:
    for i in range(n):
        if i == n-1:
            break
        else:
            if i%2 == 0:
                a = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = a
else:
    for i in range(n):
        if i%2 == 0:
            a = ls[i]
            ls[i] = ls[i+1]
            ls[i+1] = a
    
print(ls)

    

    


