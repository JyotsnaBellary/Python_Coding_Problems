List=[]      
even = []        
odd = []
a = 10
n=int(a)
for i in range(1, n+1):
    value=int(input("%d st Eleement: " %i))
    List.append(value)

for i in range(n):
    if(List[i]%2==0):
        even.append(List[i])
    else:
        odd.append(List[i])
print("list of even numbers= ",even)
print("list of odd numbers= ",odd)
