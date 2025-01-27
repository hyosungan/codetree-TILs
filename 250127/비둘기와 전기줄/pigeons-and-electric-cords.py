N=int(input())

arr=[tuple(map(int,input().split())) for _ in range(N)]

position=[2]*11
ans=0
for bird,pos in arr:
    if position[bird]!=2 and position[bird]!=pos:
        ans+=1
        position[bird]=pos
    else:
        position[bird]=pos

print(ans)



