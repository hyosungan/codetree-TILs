import sys
INT_MIN=-sys.maxsize

n = int(input())
a = list(map(int, input().split()))
count=0
ans=INT_MIN

for i in range(n):
    count+=a[i]
    ans=max(ans,count)
    if count<0:
        count=0
print(ans)
