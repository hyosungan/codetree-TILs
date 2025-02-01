from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

visited=[[0 for _ in range(n)] for _ in range(n)]

q=deque()

def is_possible(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if grid[x][y]==1:
        return False
    if visited[x][y]==1:
        return False
    return True 

def bfs():
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    while q:
        a,b=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_dx,new_dy=dx+a,dy+b
            if is_possible(new_dx,new_dy):
                visited[new_dx][new_dy]=1
                q.append((new_dx,new_dy))


for a,b in points:
    if visited[a-1][b-1]!=1:
        visited[a-1][b-1]=1
        q.append((a-1,b-1))
        bfs()
count=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==1:
            count+=1
print(count)

