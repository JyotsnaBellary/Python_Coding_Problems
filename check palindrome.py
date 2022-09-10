string = list(input("Enter the word:"))
n = len(string)
reverse = string[::-1]
if reverse == string:
    print("Is a palindrome")
else:
    print(" Not a palindrome ") 
