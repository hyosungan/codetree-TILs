import sys
input=sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix=[0]*(n+1)
prefix[1]=arr[0]
for i in range(2,n+1):
    prefix[i]=prefix[i-1]+arr[i-1]

ans=0
for i in range(1,n+1):
    for j in range(i,n+1):
        if prefix[j]-prefix[i-1]==k:
            ans+=1
print(ans)

