OFFSET=100
Max=200
width=8
arr=[[0]*(Max+1) for _ in range(Max+1)]

N=int(input())

for _ in range(N):
    x,y=map(int,input().split())
    for i in range(x+OFFSET,x+OFFSET+width):
        for j in range(y+OFFSET,y+OFFSET+width):
            arr[i][j]=1
answer=0
for i in arr:
    for j in i:
        if j==1:
            answer+=1

print(answer)