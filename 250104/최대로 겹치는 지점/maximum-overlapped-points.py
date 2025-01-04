n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr=[0]*(100+1)

for i,j in segments:
    for num in range(i,j+1):
        arr[num]+=1

print(max(arr))