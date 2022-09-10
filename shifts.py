def rshift(seq,n):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

def lshift(seq,n):
    a = n % len(seq)
    return seq[:a] + seq[-a:]

n = int(input())
a = input().split()
N = int(input())
a = [int(x) for x in a]

if N >= 0:
    a = rshift(a, N)
else:
    a = lshift(a,N)

print(a)
