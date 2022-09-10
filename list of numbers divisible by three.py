List=[]      
divisibleby3 = []
a = 20
n=int(a)
for i in range(1, n+1):
    value=int(input("%d st Eleement: " %i))
    List.append(value)

for i in range(n):
    if(List[i]%3==0):
        divisibleby3.append(List[i])
print("list of numbers divisible by 3 = ", divisibleby3)

