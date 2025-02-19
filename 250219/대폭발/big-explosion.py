n, m, r, c = map(int, input().split()) #n은 격자크기 m은 시간 r,c는 폭탄 초기 위치(x,y)좌표

r,c=r-1,c-1

bomb=[[0 for _ in range(n)] for _ in range(n)]
bomb[r][c]=1

temp=[[0 for _ in range(n)] for _ in range(n)]

dxs,dys=[-1,1,0,0],[0,0,-1,1]

def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def temp_copy():
    for i in range(n):
        for j in range(n):
            bomb[i][j]=temp[i][j]

def temp_reset():
    for i in range(n):
        for j in range(n):
            temp[i][j]=0

for t in range(1,m+1):
    for i in range(n):
        for j in range(n):
            if bomb[i][j]==1:
                temp[i][j]=1
                for dx,dy in zip(dxs,dys):
                    new_dx,new_dy=i+dx*(2**(t-1)),j+dy*(2**(t-1))
                    if is_range(new_dx,new_dy):
                        temp[new_dx][new_dy]=1
    temp_copy()
    temp_reset()

count=0
for i in range(n):
    for j in range(n):
        if bomb[i][j]==1:
            count+=1
print(count)
    


