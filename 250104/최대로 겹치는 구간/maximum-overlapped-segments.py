offset=100
max_r=200
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr=[0]*(max_r+1)

for i,j in segments:
    i,j=i+offset,j+offset
    for num in range(i,j):
        arr[num]+=1

print(max(arr))

