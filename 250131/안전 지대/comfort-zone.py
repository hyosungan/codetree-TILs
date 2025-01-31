n, m = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(n)]
top=0
for i in range(n):
    for j in range(m):
        if village[i][j]>top:
            top=village[i][j]    

visited=[[0 for _ in range(m)] for _ in range(n)]
answer=-1
answer_k=0
grid=[[0 for _ in range(m)] for _ in range(n)]

def new_grid(k):
    for i in range(n):
        for j in range(m):
            if village[i][j]>k:
                grid[i][j]=1

def is_possible(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if visited[x][y]==1:
        return False
    if grid[x][y]==0:
        return False
    return True


def dfs(x,y):
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        new_x,new_y=x+dx,y+dy
        if is_possible(new_x,new_y):
            visited[new_x][new_y]=1
            dfs(new_x,new_y)

for k in range(1,top+1):
    ans=0
    new_grid(k)
    for i in range(n):
        for j in range(m):
            if is_possible(i,j):
                visited[i][j]=1
                ans+=1
                dfs(i,j)
    #ans가 최대일때 k랑 ans를 출력해야함
    if ans>answer:
        answer=ans
        answer_k=k

    grid=[[0 for _ in range(m)] for _ in range(n)]
    visited=[[0 for _ in range(m)] for _ in range(n)]

print(answer_k,answer)

