import sys
INT_MIN=-sys.maxsize

n = int(input())
a = list(map(int, input().split()))
count=0
ans=0
dp=[INT_MIN for _ in range(n+1)]
dp[0]=0

for i in range(1,n+1):
    dp[i]=max(dp[i-1]+a[i-1],a[i-1])

print(max(dp[1:]))
