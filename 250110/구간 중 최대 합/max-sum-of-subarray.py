import sys

INT_MIN=-sys.maxsize
add=INT_MIN

n, k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n-k+1):
    sum_num=0
    for j in range(i,i+k):
        sum_num+=arr[j]
    add=max(add,sum_num)

print(add)