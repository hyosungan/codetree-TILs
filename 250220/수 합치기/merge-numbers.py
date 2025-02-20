n = int(input())
arr = list(map(int, input().split()))
ans=0
for i in range(n-1):
    a=min(arr)
    arr.remove(a)
    b=min(arr)
    arr.remove(b)
    ans+=a+b
    arr.append(a+b)

print(ans)
    

