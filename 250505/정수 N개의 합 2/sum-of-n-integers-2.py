n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans=0
prefix=[0]*n
prefix[0]=arr[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]

for i in range(n-k+1):
    ans=max(ans,prefix[i+k-1]-prefix[i]+arr[i])

print(ans)


