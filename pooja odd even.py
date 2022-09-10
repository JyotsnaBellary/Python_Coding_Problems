T = int(input())

for i in range(T):
    one = int(input())
    ones = input().split(' ')
    ones = [int(X) for X in ones]
    evens = []
    odds = []
    for each in ones:
        if each % 2 == 0:
            evens.append(each)
        else:
            odds.append(each)
    evens = evens[::-1]
    final = []
    for e in evens:
        if e % 5 == 0:
            final.append(e)
            evens.remove(e)
            print(evens)
        else:
            continue
    if len(evens) != 0:
        for e in evens:
            final.append(e)
    for o in odds:
        if o % 5 == 0:
            final.append(o)
            odds.remove(o)
    if len(evens) != 0:
        for e in odds:
            final.append(e)

    print(final)

            
