N = int(input())
test_list = input().split()

test_list.sort()
mid = N // 2
res = (int(test_list[mid]) + int(test_list[mid + 1])) 
print(res)
