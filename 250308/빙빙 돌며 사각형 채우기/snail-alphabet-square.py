n, m = map(int, input().split())
#65~90
alpha=65
dx,dy=0,0
arr=[[0 for _ in range(m)] for _ in range(n)]

dxs,dys=[0,1,0,-1],[1,0,-1,0]
direction=0

def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<m 

for _ in range(n*m):
    arr[dx][dy]=chr(alpha)
    if alpha==90:
        alpha=65
    else:
        alpha+=1
    new_x,new_y=dx+dxs[direction],dy+dys[direction]
    if is_range(new_x,new_y) and arr[new_x][new_y]==0:
        dx,dy=new_x,new_y
    else:
        direction=(direction+1)%4
        dx,dy=dx+dxs[direction],dy+dys[direction]

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()
