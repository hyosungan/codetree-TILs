import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

minus=[-i for i in arr]
heapq.heapify(minus)
for i in range(m):
    big=heapq.heappop(minus)+1
    heapq.heappush(minus,big)
print(-heapq.heappop(minus))



