import sys

INT_MAX=sys.maxsize
min_num=INT_MAX

n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    sum=0
    arr=[0]*n
    for j in range(n):
        arr[j]=abs(i-j)
        sum+=arr[j]*A[j]

    if min_num>sum:
        min_num=sum

print(min_num)

    