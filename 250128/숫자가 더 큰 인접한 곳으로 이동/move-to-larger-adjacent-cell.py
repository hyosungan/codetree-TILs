n, r, c = map(int, input().split())

r=r-1
c=c-1
arr=[list(map(int,input().split())) for _ in range(n)]

dxs,dys=[-1,1,0,0],[0,0,-1,1]


def is_range(x,y):
    return 0<=x and n>x and 0<=y and n>y

while True:
    print(arr[r][c],end=' ')
    for dx,dy in zip(dxs,dys):
        if is_range(r+dx,c+dy) and arr[r+dx][c+dy]>arr[r][c]:
            r,c=r+dx,c+dy
            break
    else:
        break




