import sys
INT_NUM=-sys.maxsize
ans=INT_NUM
X, Y = map(int, input().split())

for i in range(X,Y+1):
    sum_num=0
    i=str(i)
    for j in i:
        sum_num+=int(j)
    ans=max(ans,sum_num)

print(ans)