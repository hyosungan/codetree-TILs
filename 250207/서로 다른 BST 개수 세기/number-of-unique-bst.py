n = int(input())
dp=[0]*(n+1)

dp[0]=1
dp[1]=1


for i in range(2,n+1):
    for j in range(1,n+1):
        dp[i]+=dp[i-j]*dp[i-(i-j+1)]

print(dp[n])   