n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

arr=[0,0,0,0]

ans=0

for i in range(1,4):
    arr[i]=1
    count=0
    for j in range(n):
        arr[moves[j][0]],arr[moves[j][1]]=arr[moves[j][1]],arr[moves[j][0]]
        if arr[moves[j][2]]==1:
            count+=1
    ans=max(count,ans)
    arr=[0,0,0,0]

print(ans)
