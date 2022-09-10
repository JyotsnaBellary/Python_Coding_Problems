a = int(input())
arr = input().split(',')
arr = [int(x) for x in arr]
power = 0
arr.sort()
arr = arr[::-1]

for x in arr:
    while x - 1 in arr or x + 1 in arr:
        try:
            arr.remove(x - 1)
            arr.remove(x + 1)
        except ValueError:
            break

    power += x

    

print(power)
