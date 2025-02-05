n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs,dys=[-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for _ in range(m):
    for num in range(1,n*n+1):
        found=False
        for i in range(n):
            if found==True:
                break
            for j in range(n):
                if grid[i][j]==num:
                    max_value=-1
                    max_x,max_y=-1,-1
                    for dx,dy in zip(dxs,dys):
                        new_dx,new_dy=i+dx,j+dy
                        if is_range(new_dx,new_dy) and grid[new_dx][new_dy]>max_value:
                            max_x,max_y=new_dx,new_dy
                            max_value=grid[new_dx][new_dy]
                    grid[i][j],grid[max_x][max_y]=grid[max_x][max_y],grid[i][j]
                    found=True
                    break


for i in range(n):
    for j in range(n):
        print(grid[i][j],end=' ')
    print()

