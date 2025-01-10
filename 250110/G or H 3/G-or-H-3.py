import sys

INT_MIN=-sys.maxsize

max_num=INT_MIN

n, k = map(int, input().split())
k=k+1
arr=[0]*10001
for _ in range(n):
    pos, char = input().split()
    pos=int(pos)
    if char=='G':
        arr[pos]=1
    elif char=='H':
        arr[pos]=2

for i in range(1,10000-k+2):
    sum_num=0
    for j in range(i,i+k):
        sum_num+=arr[j]
    max_num=max(max_num,sum_num)

print(max_num)
        

