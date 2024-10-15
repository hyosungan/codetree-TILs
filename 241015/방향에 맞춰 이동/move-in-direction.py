N=int(input())


dx=[1,-1,0,0]
dy=[0,0,-1,1]
x=0
y=0

for i in range(N):
    direction=tuple(input().split())
    num=int(direction[1])
    if direction[0]=='E':
        x+=(dx[0]*num)
        y+=dy[0]
    elif direction[0]=='W':
        x+=(dx[1]*num)
        y+=dy[1]
    elif direction[0]=='S':
        x+=dx[2]
        y+=(dy[2]*num)
    elif direction[0]=='N':
        x+=dx[3]
        y+=(dy[3]*num)

print(x,y)