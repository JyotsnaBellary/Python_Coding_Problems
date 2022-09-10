ls1=[]
ls2 = []
ls = []
n=int(input("enter the number of elements for list 1:"))
for i in range(n):
    u=input("enter the elements:")
    ls1.append(u)

n=int(input("enter the number of elements for list 2:"))
for i in range(n):
    w=input("enter the elements:")
    ls2.append(w)

ls1.sort()
ls2.sort()
ls = ls1 + ls2
print(ls)
