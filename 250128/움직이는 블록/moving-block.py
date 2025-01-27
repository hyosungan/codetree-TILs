n = int(input())
blocks = [int(input()) for _ in range(n)]
ans=0
goal=(sum(blocks)//n)

for block in blocks:
    if block>goal:
        ans+=block-goal

print(ans)