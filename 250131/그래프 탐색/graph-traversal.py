n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

#visited와 graph는 인덱스의 번호가 node를 의미
visited=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node]=1
    for curr in graph[node]:
        if visited[curr]==0:
            dfs(curr)


dfs(1)

print(sum(visited)-1)