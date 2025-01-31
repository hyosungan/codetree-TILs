n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
village=[]
visited=[[0 for _ in range(n)] for _ in range(n)]


def is_possible(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if visited[x][y]==1:
        return False
    if grid[x][y]==0:
        return False
    return True

def dfs(x,y):
    global ans
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        new_x,new_y=dx+x,dy+y
        if is_possible(new_x,new_y):
            visited[new_x][new_y]=1
            dfs(new_x,new_y)

def person_check():
    count=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1:
                count+=1
    village.append(count)


for i in range(n):
    for j in range(n):
        if is_possible(i,j):
            visited[i][j]=1
            dfs(i,j)
            person_check()

for i in range(len(village)-1,0,-1):
    if len(village)>=2:
        village[i]=village[i]-village[i-1]
village.sort()
print(len(village))
for i in village:
    print(i)
