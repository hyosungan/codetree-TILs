import sys

INT_MIN=-sys.maxsize

N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp=[INT_MIN for _ in range(M+1)]
dp[0]=0

for i in range(M+1):
    for j in range(N):
        if i<coin[j]:
            continue
        if dp[i-coin[j]]==INT_MIN:
            continue
        dp[i]=max(dp[i-coin[j]]+1,dp[i])

if dp[M]==INT_MIN:
    print(-1)
else:
    print(dp[M])



