from collections import deque

#k번 bfs를 반복하는데 1번하면 그때 방문한 곳중 젤 큰 숫자가 있는곳이 다음 시작점이 됨
# 방문기록 초기화 해야하고 갈수 있는 곳은 시작점 보다 작은 숫자들만 가능
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r,c=r-1,c-1
visited=[[0 for _ in range(n)] for _ in range(n)]

q=deque()

def is_possible(x,y):
    global r,c
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if grid[x][y]>=grid[r][c]:
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
            if is_possible(new_x,new_y):
                visited[new_x][new_y]=1
                q.append((new_x,new_y))

def check_visit():
    count=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1:
                count+=1
    return count == 1

def change_start(r,c):
    max_value=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1 and not (i == r and j == c):
                if grid[i][j]>max_value:
                    new_r=i
                    new_c=j
                    max_value=grid[i][j]
    return new_r,new_c

for i in range(k):
    visited[r][c]=1
    q.append((r,c))
    bfs()
    
    if check_visit():
        print(r,c)
        break
    r,c=change_start(r,c)
    visited=[[0 for _ in range(n)] for _ in range(n)]

print(r+1,c+1)

    
    #만약  방문한 곳이 1개(자기 자신 뿐이라면 break하고 그 위치 출력)
    #아니라면 방문한곳중 제일 큰 숫자가 r,c 가됨
    #방문 기록 초기화 