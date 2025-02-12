import sys
n = int(input())
m = list(map(int, input().split()))

INT_MIN=-sys.maxsize
dp=[INT_MIN for _ in range(n)]

dp[0]=1

for i in range(1,n):
    for j in range(0,i):
        if m[i]>m[j]:
            dp[i]=max(dp[i],dp[j]+1)

ans=0
for i in range(n):
    ans=max(dp[i],ans)

print(ans)