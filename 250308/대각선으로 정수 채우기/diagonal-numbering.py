n, m = map(int, input().split())

end=n*m
start=1

arr=[[0 for _ in range(m)] for _ in range(n)]

while start<=end:
    break_num=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                check=(i,j)
                arr[i][j]=start
                start+=1
                break_num=1
                break
        if break_num==1:
            break
    
    for _ in range(1,n):
        check=(check[0]+1,check[1]-1)
        if check[0]>=0 and check[0]<n and check[1]>=0 and check[1]<m:
            arr[check[0]][check[1]]=start
            start+=1
        else:
            break

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()

            
