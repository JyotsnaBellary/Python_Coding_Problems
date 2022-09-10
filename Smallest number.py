n=int(input("total number of list elements: "))
List = []
for i in range(0, n):
    value=int(input("%d st Eleement: " %i))
    List.append(value)
List.sort()
print(List[0])
