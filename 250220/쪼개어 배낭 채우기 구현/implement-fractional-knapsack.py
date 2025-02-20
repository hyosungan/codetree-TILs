N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)
arr=[]
ans=0
for i in range(N):
    arr.append([i,v[i]/w[i]])
arr.sort(key=lambda x: -x[1])

for idx,temp in arr:
    if M<w[idx]:
        ans+=(M/w[idx])*v[idx]
        break
    ans+=v[idx]
    M-=w[idx]

print(f"{round(ans,3):.3f}")

