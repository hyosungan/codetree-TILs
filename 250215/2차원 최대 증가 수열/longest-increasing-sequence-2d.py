import sys

INT_MIN=-sys.maxsize

n,m=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]

dp=[[INT_MIN for _ in range(m)] for _ in range(n)]

dp[0][0]=1



for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        for k in range(i):
            for l in range(j):
                if dp[k][l]==INT_MIN:
                    continue
                if arr[k][l]<arr[i][j]:
                    dp[i][j]=max(dp[i][j],dp[k][l]+1)

ans=0
for i in range(n):
    for j in range(m):
        ans=max(dp[i][j],ans)
print(ans)

