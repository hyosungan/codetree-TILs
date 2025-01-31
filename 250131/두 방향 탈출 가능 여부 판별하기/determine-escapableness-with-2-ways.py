n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)] #뱀의 유무
ans=0
visited=[[0 for _ in range(m)] for _ in range(n)]

def is_possible(x,y):
    #범위에 있는지 뱀있는지 방문한적이 없는지
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if grid[x][y]==0:
        return False
    if visited[x][y]==1:
        return False
    return True 

def dfs(x,y):
    global ans
    if x==n-1 and y==m-1:
        ans=1
        return

    dxs,dys=[1,0],[0,1]
    for dx,dy in zip(dxs,dys):
        new_dx,new_dy=x+dx,y+dy
        if is_possible(new_dx,new_dy):
            visited[new_dx][new_dy]=1
            dfs(new_dx,new_dy)

visited[0][0]=1
dfs(0,0)
print(ans)
