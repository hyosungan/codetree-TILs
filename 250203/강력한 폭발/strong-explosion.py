import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=0
bomb=[]
new_grid = copy.deepcopy(grid)  # 깊은 복사 사용
bomb_shape=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            bomb.append((i,j))


def is_range(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    return True

def shape(x,y,n):
    if n==1:
        dxs,dys=[-1,-2,1,2],[0,0,0,0]
    if n==2:
        dxs,dys=[-1,1,0,0],[0,0,-1,1]
    if n==3:
        dxs,dys=[-1,-1,1,1],[-1,1,-1,1]
    for dx,dy in zip(dxs,dys):
        if is_range(x+dx,y+dy):
            grid[x+dx][y+dy]=1
def find_bomb_site():
    count=0
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                count+=1
    return count

def choose(idx):
    global grid,ans
    if idx == len(bomb):
        for (x, y), num in zip(bomb, bomb_shape):
            shape(x, y, num)
        ans = max(ans, find_bomb_site())
        grid = copy.deepcopy(new_grid)  # 원본 복구
        return
    for i in range(1,4):
        bomb_shape.append(i)
        choose(idx+1)
        bomb_shape.pop()

choose(0)
print(ans)
        

