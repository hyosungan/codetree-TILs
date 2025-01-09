R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

start=grid[0][0]
ans=0
for i in range(1,R):
    for j in range(1,C):
        if grid[i][j] != start:
            for k in range(i+1,R):
                for l in range(j+1,C):
                    if grid[k][l]!=grid[i][j]:
                        if grid[k][l]!=grid[R-1][C-1] and k<=R-2 and l<=C-2:
                            ans+=1 

print(ans)

