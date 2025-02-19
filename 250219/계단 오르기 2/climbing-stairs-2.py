import sys
INT_MIN=-sys.maxsize

n = int(input())
a = [0] + list(map(int, input().split()))


dp=[[INT_MIN for _ in range(4)] for _ in range(n+1)]

dp[0][0]=0

for i in range(1,n+1):
    for j in range(4):
        if i<j:
            continue
        if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
            continue
        if j==0:
            dp[i][j]=dp[i-2][j]+a[i]
            continue
        if i==1 and j==1:
            dp[i][j]=a[i]
            continue

        dp[i][j]=max(dp[i-1][j-1]+a[i],dp[i-2][j]+a[i])

print(max(dp[n]))