ls=[]
count = {}
n=int(input("enter the number of integers:"))
for i in range(n):
    w=input("enter the integer:")
    ls.append(w)
a = 0


'''
for i in range(n):
    if i == n-1:
        if ls[i-1] == ls[i]:
            count[ls[i]] += 1
            break
        else:
            count[ls[i]] = 1
    else:
        if ls[i-1] == ls[i]:
            count[ls[i-1]] += 1
        else:
            count[ls[i]] = 1
print(count)
