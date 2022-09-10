def maxAbsoluteDiff(a,n):
    max = 0
    lst = []
    for i in range(n-1):
        for j in range(n):
            if a[i] != a[j]:
                lst.append([a[i],a[j]])

    rlst = []
    diff = []
    for ele in lst:
        l = []
        for e in ele:
            e = str(e)
            a = e[::-1]
            l.append(a)
        rlst.append(l)

        diff.append(abs(int(l[1]) - int(l[0])))
    print(type(diff[0]))
    

    
n = int(input("N:"))
a = input().split(" ")

maxAbsoluteDiff(a, n)
