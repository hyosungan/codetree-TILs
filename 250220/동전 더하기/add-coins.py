n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
ans=0


for coin in coins:
    if k==0:
        break
    count=k//coin
    ans+=count
    k-=count*coin

print(ans)
