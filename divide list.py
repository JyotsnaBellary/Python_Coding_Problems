ls=[]
ls1=[]
ls2=[]
n = int(input('Enter number of elements:'))
for i in range(n):
    w = int(input('enter element:'))
    ls.append(w)
    
for i in range(int(n/2)):
    ls1.append(ls[i])

for element in ls:
    if element not in ls1:
        ls2.append(element)
print(ls)
print(ls1)
print(ls2)

    
    
    
