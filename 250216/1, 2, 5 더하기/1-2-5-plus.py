import sys
INT_MIN=-sys.maxsize

n = int(input())

dp=[0 for _ in range(n+1)]

dp[0]=1

for i in range(1,n+1):
    for j in [1,2,5]:
        if i-j<0:
            continue
        if dp[i-j]==0:
            continue
        dp[i]+=dp[i-j]
    dp[i]%=10007

print(dp[n])

