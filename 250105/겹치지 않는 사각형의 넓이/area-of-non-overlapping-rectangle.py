OFFSET=1000

arr=[[0]*2001 for _ in range(2001)]

for _ in range(2):
     
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1+OFFSET,x2+OFFSET):
        for j in range(y1+OFFSET,y2+OFFSET):
            arr[i][j]=1


x_1,y_1,x_2,y_2=map(int,input().split())    
for i in range(x_1+OFFSET,x_2+OFFSET):
        for j in range(y_1+OFFSET,y_2+OFFSET):
            arr[i][j]=0
answer=0
for i in arr:
    for j in i:
        if j==1:
            answer+=1
print(answer)    
