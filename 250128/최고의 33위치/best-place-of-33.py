n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def count_coin(row,col):
    coin=0
    for i in range(row,row+3):
        for j in range(col,col+3):
            if grid[i][j]==1:
                coin+=1
    return coin

ans=0
for i in range(n):
    for j in range(n):
        if i+2>=n or j+2>=n:
            continue
        ans=max(ans,count_coin(i,j))

print(ans)
