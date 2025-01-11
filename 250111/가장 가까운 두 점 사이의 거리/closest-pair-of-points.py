import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans=sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        distance=((points[i][0]-points[j][0])*(points[i][0]-points[j][0])
        +(points[i][1]-points[j][1])*(points[i][1]-points[j][1]))
        ans=min(ans,distance)

print(ans)

