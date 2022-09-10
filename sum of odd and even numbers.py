List=[23,5,7,8,45,98,67,45,64,2]      
evenSum=0        
oddSum=0        
for item in List:
    if(item%2==0):
        evenSum=evenSum+item
    else:
        oddSum=oddSum+item
print("sum of even numbers= ",evenSum)
print("sum of odd numbers= ",oddSum)
