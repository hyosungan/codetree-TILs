n, m, t = map(int, input().split())

# Create n x n grid
arr = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
curr = [[0]*(n+1) for _ in range(n+1)]

for a,b, in marbles:
    curr[a][b]=1

next_arr=[[0]*(n+1) for _ in range(n+1)]

def is_range(x,y):
    return x>=1 and x<=n and y>=1 and y<=n

def possible(i,j):
    max_x=0
    max_y=0
    max_value=0
    dxs,dys=[-1,1,0,0],[0,0,-1,1]
    for dx,dy in zip(dxs,dys):
        if is_range(i+dx,j+dy):
            if arr[i+dx][j+dy]>max_value:
                max_x=i+dx
                max_y=j+dy
                max_value=arr[i+dx][j+dy]
    
    next_arr[max_x][max_y]+=1

def copy():
    for i in range(1,n+1):
        for j in range(1,n+1):
            curr[i][j]=next_arr[i][j]

def remove_double():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if next_arr[i][j]>=2:
                curr[i][j]=0

def move():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if curr[i][j]==1:
                possible(i,j)
    copy()
    remove_double()            

for _ in range(t):
    move()

count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if curr[i][j]==1:
            count+=1

print(count)

        



