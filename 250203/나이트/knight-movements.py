from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

q=deque()
visited=[[0 for _ in range(n)] for _ in range(n)]
step=[[0 for _ in range(n)] for _ in range(n)]

def is_possible(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if visited[x][y]==1:
        return False
    return True

def bfs():
    dxs,dys=[-2,-2,2,2,1,-1,1,-1],[-1,1,-1,1,-2,-2,2,2]
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_x,new_y=x+dx,y+dy
            if is_possible(new_x,new_y):
                visited[new_x][new_y]=1
                q.append((new_x,new_y))
                step[new_x][new_y]=step[x][y]+1

q.append((r1-1,c1-1))
visited[r1-1][c1-1]=1
bfs()

if visited[r2-1][c2-1]==1:
    print(step[r2-1][c2-1])
else:
    print(-1)


