import sys
INT_MAX=sys.maxsize

N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp=list(INT_MAX for _ in range(M+1))

dp[0]=0

for i in range(1,M+1):
    for j in range(N):
        if i<coin[j]:
            continue
        if dp[i-coin[j]]==INT_MAX:
            continue
        dp[i]=min(dp[i-coin[j]]+1,dp[i])

if dp[M]==INT_MAX:
    print(-1)
else:
    print(dp[M])



