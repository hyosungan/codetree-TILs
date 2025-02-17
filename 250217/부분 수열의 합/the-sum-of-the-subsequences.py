n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp=[0 for _ in range(m+1)]
dp[0]=1
for i in range(n):
    for j in range(m,0,-1):
        if j<arr[i]:
            continue
        if dp[j-arr[i]]==0:
            continue
        dp[j]=1

if dp[m]==1:
    print("Yes")
else:
    print("No")
