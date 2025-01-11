import sys
INT_MAX=-sys.maxsize
INT_MIN=sys.maxsize

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans=INT_MIN
for i in range(n):
    max_num_x=INT_MAX
    min_num_x=INT_MIN
    max_num_y=INT_MAX
    min_num_y=INT_MIN
    for j in range(n):
        if i==j:
            continue
        max_num_x=max(points[j][0],max_num_x)
        min_num_x=min(points[j][0],min_num_x)
        max_num_y=max(points[j][1],max_num_y)
        min_num_y=min(points[j][1],min_num_y)
    size=(max_num_x-min_num_x)*(max_num_y-min_num_y)

    ans=min(size,ans)
print(ans)






