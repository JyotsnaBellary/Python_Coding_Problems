Str = list(input("Enter the string:").split('-'))
print(Str)
Str.sort()
str1 = []
for element in Str:
    str1.append(element)
    if element != Str[-1]:
        str1.append('-')

print(''.join(word for word in str1))



        
