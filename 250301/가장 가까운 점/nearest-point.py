import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

pq=[]


for x,y in points:
    heapq.heappush(pq,(x+y,x,y))

for _ in range(m):
    x_y,x,y=heapq.heappop(pq)
    heapq.heappush(pq,(x_y+4,x+2,y+2))

a=heapq.heappop(pq)
print(a[1],a[2])

