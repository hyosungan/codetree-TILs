dirs = input()

x,y=0,0
direction=0
dx,dy=[0,1,0,-1],[1,0,-1,0]

for letter in dirs:
    if letter=='L':
        direction=(direction+3)%4
    elif letter=='R':
        direction=(direction+1)%4
    else:
        x,y=x+dx[direction],y+dy[direction]

print(x,y)