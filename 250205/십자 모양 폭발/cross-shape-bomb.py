n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r,c=r-1,c-1

dxs,dys=[-1,1,0,0],[0,0,-1,1]

length=grid[r][c]
temp=[[0 for _ in range(n)] for _ in range(n)]
def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<n


for dx,dy in zip(dxs,dys):
    for i in range(length):
        if is_range(r+dx*i,c+dy*i):
            grid[r+dx*i][c+dy*i]=0


for j in range(n):
    idx=n-1
    for i in range(n-1,-1,-1):
        if grid[i][j]!=0:
            temp[idx][j]=grid[i][j]
            idx-=1            



for i in range(n):
    for j in range(n):
        print(temp[i][j],end=' ')
    print()
    

