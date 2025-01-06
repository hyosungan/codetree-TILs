N=int(input())
dx,dy=[1,-1,0,0],[0,0,-1,1]
x,y=0,0
for _ in range(N):
    direction, move=input().split()
    if direction=='N':
        x+=dx[3]*int(move)
        y+=dy[3]*int(move)

    if direction=='W':
        x+=dx[1]*int(move)
        y+=dy[1]*int(move)
    if direction=='S':
        x+=dx[2]*int(move)
        y+=dy[2]*int(move)
    if direction=='E':
        x+=dx[0]*int(move)
        y+=dy[0]*int(move)
print(x,y)






