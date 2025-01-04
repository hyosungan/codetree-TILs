OFFSET=100
arr=[[0]*101 for _ in range(101)]
n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a,c):
        for j in range(b,d):
            arr[i][j]=1
answer=0
for i in range(101):
    for j in range(101):
        if arr[i][j]==1:
            answer+=1

print(answer)
   

