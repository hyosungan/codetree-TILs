n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans=0
def triangle(i1,i2,i3):
    x1,y1=points[i1]
    x2,y2=points[i2]
    x3,y3=points[i3]
    if (x1==x2 or x1==x3 or x2==x3) and (y1==y2 or y2==y3 or y1==y3):
        return (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)
    else:
        return 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            ans=max(ans,triangle(i,j,k))

print(ans)


