import sys
INT_MIN=-sys.maxsize

n,k=map(int,input().split())

a=[0]+list(map(int,input().split()))

dp=[[INT_MIN for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    
    #a[i]가 양수
    if a[i]>=0:
        for j in range(k+1):
            dp[i][j]=max(dp[i-1][j]+a[i],a[i])


    #a[i]가 음수
    else:
        for j in range(1,k+1):
            dp[i][j]=max(dp[i-1][j-1]+a[i],a[i])
    
ans=INT_MIN
for i in range(n+1):
    for j in range(k+1):
        ans=max(dp[i][j],ans)

print(ans)