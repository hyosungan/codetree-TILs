from collections import deque

n,k= map(int,input().split())
answer=0
grid=[[int(x) for x in input().split()] for _ in range(n)]

point=[[int(x)-1 for x in input().split()] for _ in range(k)]

visited=[[0 for _ in range(n)] for _ in range(n)]

q=deque()

def bfs():
    dxs=[1,-1,0,0]
    dys=[0,0,-1,1]
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            new_x,new_y=x+dx,y+dy
            if is_ok(new_x,new_y):
                push(new_x,new_y)

def is_ok(x,y):
    return in_range(x,y) and visited[x][y]==0 and grid[x][y]==0

def in_range(x,y):
    return x<n and x>=0 and y>=0 and y<n

def push(x,y):
    visited[x][y]=1
    q.append((x,y))

for i in point:
    push(i[0],i[1])
    bfs()

for i in visited:
    answer+=i.count(1)
print(answer)