import sys,heapq

N, M = map(int, input().split())
pq=[]
dist=[int(1e9) for _ in range(N+1)]
dist[N]=0
heapq.heappush(pq,(0,N)) #거리와 노드 번호

edges=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,d=map(int,input().split())
    edges[b].append((a,d))

while pq:
    curr_dist,curr_node=heapq.heappop(pq)
    # if dist[curr_node]!=curr_dist:
    #     continue
    for next_node,next_dist in edges[curr_node]:
        if dist[next_node]>curr_dist+next_dist:
            dist[next_node]=curr_dist+next_dist
            heapq.heappush(pq,(curr_dist+next_dist,next_node))

print(max(dist[1:]))





