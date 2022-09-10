def dectoOct(decimal):
    if(decimal > 0):
        dectoOct((int)(decimal/8))
        print(decimal%8, end='')
        
decimal = int(input("Enter a decimal number: "))
print("Octal: ", end='')
dectoOct(decimal)
