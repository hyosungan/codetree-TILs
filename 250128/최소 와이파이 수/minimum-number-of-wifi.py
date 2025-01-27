n, m = map(int, input().split())
arr = list(map(int, input().split()))


#가다가 0은패스하고 1이 나오면 m 거리 뒤에 설치
ans=0
start=0
while True:
    if arr[start]==1:
        start+=(2*m)
        ans+=1
    start+=1
    if start>n-1:
        break

print(ans)
