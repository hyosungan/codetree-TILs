n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for time in range(t):
    temp=d[-1]
    for i in range(n-1,0,-1):
        d[i]=d[i-1]
    d[0]=r[-1]
    for i in range(n-1,0,-1):
        r[i]=r[i-1]
    r[0]=l[-1]

    for i in range(n-1,0,-1):
        l[i]=l[i-1]
    l[0]=temp

for i in l:
    print(i,end=' ')
print()
for i in r:
    print(i,end=' ')
print()
for i in d:
    print(i,end=' ')





