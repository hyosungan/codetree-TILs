n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=0

block_x,block_y=[[0,1,1],[0,0,1],[0,0,1],[0,0,-1],[0,1,2],[0,0,0]],[[0,0,1],[0,1,1],[0,1,0],[0,1,1],[0,0,0],[0,1,2]]

def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

for i in range(n):
    for j in range(m):
        for k in range(6):
            for x,y in zip(block_x[k],block_y[k]):
                if is_range(i+x,j+y)==False:
                    break
            else:
                ans=max(ans,grid[block_x[k][0]+i][block_y[k][0]+j]+grid[block_x[k][1]+i][block_y[k][1]+j]+grid[block_x[k][2]+i][block_y[k][2]+j])

print(ans)