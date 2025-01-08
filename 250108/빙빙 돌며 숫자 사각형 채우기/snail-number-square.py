n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dxs,dys=[0,1,0,-1],[1,0,-1,0] #동서남북 순으로 

arr[0][0]=1
x,y=0,0
now_d=0 #동쪽 먼저 시작 

def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

for i in range(2,n*m+1):
    nx,ny=x+dxs[now_d],y+dys[now_d]
    if is_range(nx,ny)==False or arr[nx][ny]!=0:
        now_d=(now_d+1)%4
    x,y=x+dxs[now_d],y+dys[now_d]
    arr[x][y]=i

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()


