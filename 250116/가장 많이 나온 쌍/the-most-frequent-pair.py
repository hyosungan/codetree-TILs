n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]
ans=0
for i in range(n):
    for j in range(n):
        if i!=j:
            count=0
            for a,b in pairs:
                if (a==i and b==j) or (a==j and b==i):
                    count+=1

            ans=max(ans,count)
print(ans) 
