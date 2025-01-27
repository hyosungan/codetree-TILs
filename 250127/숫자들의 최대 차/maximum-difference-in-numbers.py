import sys
MAX_NUM=sys.maxsize
ans=-MAX_NUM

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

for i in range(0,len(arr)):
    count=1
    for j in range(i+1,len(arr)):
        if arr[j]-arr[i]<=K:
            count+=1
    
    ans=max(count,ans)

print(ans)
