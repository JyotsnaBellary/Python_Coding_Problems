allGuests = {'Alice': {'apples': 5, 'cups': 12}, 'Bob': {'sandwiches': 3,
'apples': 2}, 'Carol': {'cups': 3, 'apple pies':1}}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
        return numBrought


print('Number of things being brought:')
print(' - Apples ', totalBrought(allGuests, 'apples'))
print(' - Cups ' , totalBrought(allGuests, 'cups'))
print(' - Cakes ' , totalBrought(allGuests, 'cakes'))
print(' - Sandwiches', totalBrought(allGuests, 'sandwiches'))
print(' - Apple Pies ' ,totalBrought(allGuests, 'apple pies'))
