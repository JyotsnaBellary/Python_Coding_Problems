n=int(input("total number of list elements: "))
List = []
for i in range(1, n+1):
    value=int(input("%d st Eleement: " %i))
    List.append(value)
y = int(input("element to be searched:"))
count = 0
for item in List:
    if(item == y):
        count = count + 1
print("the number of times", y ,"has repeated in the list is", count)

