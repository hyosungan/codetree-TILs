from collections import deque

n,m=map(int,input().split())

grid = [[int(x) for x in input().split()] for _ in range(n)]

# n, m = tuple(map(int, input().split()))

# grid = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

visited=[[False for _ in range(m)] for _ in range(n)]

q=deque()


def bfs():
    
    while q:
        x,y=q.popleft()
        dxs=[1,-1,0,0]
        dxy=[0,0,-1,1]
        for dx,dy in zip(dxs,dxy):
            new_x,new_y=x+dx,y+dy
            if is_ok(new_x,new_y):
                push(new_x,new_y)


def is_ok(x,y):
    if in_range(x,y)==False:
        return False
    if grid[x][y]==0:
        return False
    if visited[x][y]==True:
        return False
    
    return True

def in_range(x,y):
    if x<n and x>=0 and y<m and y>=0:
        return True
    return False

def push(x,y):
    visited[x][y]=True
    q.append((x,y))
    

push(0,0)
bfs()

answer=1 if visited[n - 1][m - 1] else 0

print(answer)