n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for i in range(t):
    temp=d[-1]
    for j in range(n-1,0,-1):
        d[j]=d[j-1]

    d[0]=u[-1]
    for k in range(n-1,0,-1):
        u[k]=u[k-1]
    u[0]=temp

for i in u:
    print(i,end=' ')
print()
for i in d:
    print(i,end=' ')




