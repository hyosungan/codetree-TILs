n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

arr=[[0 for _ in range(n)] for _ in range(n)]
arr[0][n-1]=grid[0][n-1]
for j in range(n-2,-1,-1):
    arr[0][j]=grid[0][j]+arr[0][j+1]

for i in range(1,n):
    arr[i][n-1]=grid[i][n-1]+arr[i-1][n-1]

for i in range(1,n):
    for j in range(n-2,-1,-1):
        arr[i][j]=min(arr[i-1][j],arr[i][j+1])+grid[i][j]

# for i in range(n):
#     for j in range(n):
#         print(arr[i][j],end=' ')
#     print()
print(arr[n-1][0])


        
