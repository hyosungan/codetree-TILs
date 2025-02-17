import sys
INT_MIN=-sys.maxsize

n = int(input())
profit = [0]+list(map(int, input().split()))

dp=[INT_MIN for _ in range(n+1)]

dp[0]=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if i<j:
            continue
        # if dp[i-j]==INT_MIN:
        #     continue
        dp[i]=max(dp[i],dp[i-j]+profit[j])

print(dp[n])


