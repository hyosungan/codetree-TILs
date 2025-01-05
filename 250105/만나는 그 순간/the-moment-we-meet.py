n, m = map(int, input().split())

a = [0]
b = [0]
now_a=0
now_b=0
for _ in range(n):
    direction_a, time_a = input().split()
    for i in range((int(time_a))):
        if direction_a=='R':
            now_a+=1
            a.append(now_a)
        else:
            now_a-=1
            a.append(now_a)    

for _ in range(m):
    direction_b, time_b = input().split()
    for i in range((int(time_b))):
        if direction_b=='R':
            now_b+=1
            b.append(now_b)
        else:
            now_b-=1
            b.append(now_b)

ans=0
for i,j in zip(a,b):
    if ans==0:
        ans+=1
        continue
    if i==j:
        print(ans)
        break
    ans+=1
else:
    print(-1)