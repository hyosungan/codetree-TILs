import sys
INT_MIN=-sys.maxsize

n, k = map(int, input().split())
a = [0]+list(map(int, input().split()))

dp=[0 for _ in range(n+1)]

dp[0]=0

count=0
for i in range(1,n+1):
    if a[i]<0:
        count+=1
    if count>k:
        for j in range(i-1,0,-1):
            if a[j]<0:
                for k in range(j+1,i+1):
                    dp[i]+=a[k]
                break
        count=1
        continue
    dp[i]=max(a[i],dp[i-1]+a[i])
    if dp[i]==a[i]:
        if dp[i]<0:
            count=1
        else:
            count=0

print(max(dp))


