import sys

INT_MIN=-sys.maxsize

n=int(input())

arr=list(map(int,input().split()))

dp=[INT_MIN for _ in range(n)]
dp[0]=0

for i in range(1,n):
    for j in range(i):
        if dp[j]==INT_MIN:  #이 조건으로 끊기는 경우에도 올바르게 처리 가능
            continue

        if arr[j]+j>=i:
            dp[i]=max(dp[j]+1,dp[i])

print(max(dp))

