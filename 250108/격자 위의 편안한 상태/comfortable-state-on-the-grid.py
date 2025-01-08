n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

arr=[[0]*n for _ in range(n)]


dxs,dys=[0,0,1,-1],[1,-1,0,0]

def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for x,y in points:
    x,y=x-1,y-1
    count=0
    for dx, dy in zip(dxs,dys):
        nx,ny= x+dx, y+dy
        if is_range(nx,ny) and arr[nx][ny]==1:
            count+=1
    if count==3:
        print(1)
    else:
        print(0)
    arr[x][y]=1


