n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

arr=[]
for i in range(s1-1,e1):
    blocks[i]=0

for i in range(n):
    if blocks[i]!=0:
        arr.append(blocks[i])


for j in range(s2-1,e2):
    arr[j]=0

count=0
for k in range(len(arr)):
    if arr[k]!=0:
        count+=1

print(count)

for k in range(len(arr)):
    if arr[k]!=0:
        print(arr[k])