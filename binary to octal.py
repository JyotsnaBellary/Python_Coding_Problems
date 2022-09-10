print("Enter the Binary Number: ", end="")
bnum = int(input())

odig = 0
mul = chk = 1
onum = ""
while bnum!=0:
    rem = bnum % 10
    odig = odig + (rem * mul)
    if chk%3==0:
        onum = onum + str(odig)
        mul = chk = 1
        odig = 0
    else:
        mul = mul*2
        chk = chk+1
    bnum = int(bnum / 10)

if chk!=1:
    onum = onum + str(odig)

print("\nEquivalent Octal Value = ", onum[::-1])
