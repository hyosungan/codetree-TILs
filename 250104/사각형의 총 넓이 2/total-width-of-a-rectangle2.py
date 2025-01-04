OFFSET=100
arr=[[0]*201 for _ in range(201)]
n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a+100,c+100):
        for j in range(b+100,d+100):
            arr[i][j]=1
answer=0
for i in range(201):
    for j in range(201):
        if arr[i][j]==1:
            answer+=1

print(answer)
   

