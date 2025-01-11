n = int(input())
arr = list(map(int, input().split()))
ans=0
for i in range(n):  #시작점
    for j in range(i,n): #끝점
        avg=0
        for k in range(i,j+1):  #시작점과 끝점사이 더하는 for문
            avg+=arr[k]
        
        avg=avg/(j+1-i)
        
        for t in range(i,j+1):
            if avg==arr[t]:
                ans+=1
                break

print(ans)