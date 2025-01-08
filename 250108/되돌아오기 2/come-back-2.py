commands = input()

dxs, dys=[0,1,0,-1],[1,0,-1,0]

now_d=0
x,y=0,0

ans=0
for i in commands:
    if i=='L':
        now_d=(now_d+3)%4
        ans+=1
    elif i=='R':
        now_d=(now_d+1)%4
        ans+=1

    else:
        x,y=x+dxs[now_d],y+dys[now_d]
        ans+=1
    if x==0 and y==0:
        break

print(ans)
    