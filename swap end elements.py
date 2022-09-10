ls=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    ele=input("enter the elements:")
    ls.append(ele)
ls[0],ls[n-1]=ls[n-1],ls[0]
print(ls)
