from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited=[[0 for _ in range(m)] for _ in range(n)]

q=deque()

def is_possible(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if grid[x][y]==0:
        return False
    if visited[x][y]==1:
        return False
    return True

def bfs(x,y):
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    while q:
        a,b=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_dx,new_dy=a+dx,b+dy
            if is_possible(new_dx,new_dy):
                visited[new_dx][new_dy]=1
                q.append((new_dx,new_dy))
    
    


visited[0][0]=1
q.append((0,0))
bfs(0,0)
if visited[n-1][m-1]==1:
    print(1)
else:
    print(0) 




