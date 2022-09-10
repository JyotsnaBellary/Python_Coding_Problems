def common(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
lst1 = []
lst2 = []
n = int(input("range="))
for i in range(0, n): 
    ele = int(input("%d element=" %i)) 
  
    lst1.append(ele)
    
for i in range(0, n): 
    ele = int(input("%d element=" %i)) 
  
    lst2.append(ele)
    
print(common(lst1, lst2))
