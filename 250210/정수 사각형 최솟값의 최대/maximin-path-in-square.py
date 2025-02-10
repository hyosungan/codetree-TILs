n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

#타켓 지점은 위랑 왼쪽이랑 중에 큰걸택하고 그다음 자기자신이랑 비교해서 작은걸 적음
#초기화 할때는 자기자신이랑 전에 적혀있던 것중 작은거를 적어둠

arr=[[0 for _ in range(n)] for _ in range(n)]

arr[0][0]=grid[0][0]

for i in range(1,n):
    arr[i][0]=min(arr[i-1][0],grid[i][0])

for j in range(1,n):
    arr[0][j]=min(grid[0][j],arr[0][j-1])

for i in range(1,n):
    for j in range(1,n):
        arr[i][j]=min(grid[i][j],max(arr[i-1][j],arr[i][j-1]))

print(arr[n-1][n-1])