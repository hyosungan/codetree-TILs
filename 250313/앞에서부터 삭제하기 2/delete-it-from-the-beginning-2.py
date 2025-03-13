import heapq

n = int(input())
arr = list(map(int, input().split()))
ans=0

for k in range(1,n-1):
    candidate=arr[k:]
    heapq.heapify(candidate)
    heapq.heappop(candidate)
    avg=sum(candidate)/len(candidate)
    ans=max(ans,avg)

print(f"{ans:.2f}")
    

    