import heapq

n = int(input())
arr = list(map(int, input().split()))

pq=[]
for i in arr:
    heapq.heappush(pq,-i)

while True:
    if len(pq)<2:
        if len(pq)==1:
            print(-pq[0])
        else:
            print(-1)
        break
    a=-heapq.heappop(pq)
    b=-heapq.heappop(pq)
    if a==b:
        pass
    else:
        heapq.heappush(pq,-abs(a-b))
