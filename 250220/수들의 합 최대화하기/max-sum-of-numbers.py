n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited=[0 for _ in range(n)]
ans=0
def recur(idx,value):
    global ans
    if idx==n:
        ans=max(ans,value)
        return

    
    for j in range(n):
        if visited[j]==1:
            continue
        visited[j]=1
        value+=grid[idx][j]
        recur(idx+1,value)
        visited[j]=0
        value-=grid[idx][j]

recur(0,0)

print(ans)
