ls = []
n=int(input("enter the number of elements:"))
for i in range(n):
    e=input("enter the elements:")
    ls.append(e)

count = 0
for item in ls:
    if type(item) == tuple():
        break
    else:
        count = count + 1
        
print(count)
