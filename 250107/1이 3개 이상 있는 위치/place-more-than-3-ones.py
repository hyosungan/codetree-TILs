n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs,dys=[0,1,0,-1],[1,0,-1,0]


def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

ans=0
for i in range(n):
    for j in range(n):
        count=0
        for dx,dy in zip(dxs,dys):
            if is_range(i+dx,j+dy) and grid[i+dx][j+dy]==1:
                count+=1

        if count>=3:
            ans+=1

print(ans)
    

