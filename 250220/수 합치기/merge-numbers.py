n = int(input())
arr = list(map(int, input().split()))
ans=0


for i in range(n-1):
    arr.sort(key=lambda x:-x)
    a=arr.pop()
    b=arr.pop()
    ans+=a+b
    arr.append(a+b)

print(ans)
    

