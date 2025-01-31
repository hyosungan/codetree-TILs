import sys

sys.setrecursionlimit(3000)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited=[[0 for _ in range(n)] for _ in range(n)]
ans=0
max_num=0
count=0
def is_possible(x,y,k):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if grid[x][y]!=k:
        return False
    if visited[x][y]==1:
        return False
    return True

def bomb(max_num):
    global count
    if max_num>=4:
        return True
    else:
        return False


def dfs(x,y,k):
    global max_num
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        new_x,new_y=x+dx,y+dy
        if is_possible(new_x,new_y,k):
            max_num+=1
            visited[new_x][new_y]=1
            dfs(new_x,new_y,k)


for k in range(1,101):
    for i in range(n):
        for j in range(n):
            if is_possible(i,j,k):
                max_num+=1
                visited[i][j]=1
                dfs(i,j,k)
                if bomb(max_num):  #4개 이상 붙어있을때 
                    count+=1
                ans=max(max_num,ans)
                max_num=0
    visited=[[0 for _ in range(n)] for _ in range(n)]

print(count,ans)

