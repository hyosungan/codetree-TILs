from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited=[[0 for _ in range(m)]for _ in range(n)]
step=[[0 for _ in range(m)]for _ in range(n)]

q=deque()

def is_posible(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if grid[x][y]==0:
        return False
    if visited[x][y]==1:
        return False
    return True

def bfs():
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_x,new_y=x+dx,y+dy
            if is_posible(new_x,new_y):
                visited[new_x][new_y]=1
                q.append((new_x,new_y))
                step[new_x][new_y]=step[x][y]+1

q.append((0,0))
visited[0][0]=1
bfs()

if visited[n-1][m-1]==1:
    print(step[n-1][m-1])
else:
    print(-1)


