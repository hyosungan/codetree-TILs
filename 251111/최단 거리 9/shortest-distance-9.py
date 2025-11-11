import heapq

N, M = map(int, input().split())

edges = [[] for _ in range(N+1)]
pq=[]
for _ in range(M):
    s,e,c=map(int, input().split())
    edges[s].append((e,c))
    edges[e].append((s,c))
A, B = map(int, input().split())

dist=[int(1e9) for _ in range(N+1)]
dist[A]=0
path=[-1]*(N+1)
heapq.heappush(pq,(0,A)) #비용, 노드

while pq:
    cost,node=heapq.heappop(pq)
    
    if cost!=dist[node]:
        continue
    for elem,c in edges[node]:
        if dist[elem]>cost+c:
            dist[elem]=cost+c
            heapq.heappush(pq,(cost+c,elem))
            path[elem]=node
ans=[]            
ans.append(B)
x=B
while x!=A:
    x=path[x]
    ans.append(x)

print(max(dist[1:]))
print(*ans[::-1])


