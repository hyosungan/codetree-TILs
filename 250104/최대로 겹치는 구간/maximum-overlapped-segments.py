n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr=[0]*9999

for i in segments:
    for num in range(i[0],i[1]):
        arr[num]+=1

print(max(arr))

