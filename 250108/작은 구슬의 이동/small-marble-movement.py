n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r)-1, int(c)-1

directions={'U':0, 'R':1,'L':2,'D':3}
now_d=directions[d] #0,1,2,3
dx,dy=[-1,0,0,1],[0,1,-1,0]

def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for _ in range(t):
    nr,nc=r+dx[now_d],c+dy[now_d]
    if is_range(nr,nc):
        r,c=nr,nc
        
    else:
        now_d=3-now_d

print(r+1,c+1)





