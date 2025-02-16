import sys
sys.setrecursionlimit(20000)
INT_MAX=sys.maxsize

N, M = map(int, input().split())
coin = list(map(int, input().split()))
ans=INT_MAX
def recur(value,count):
    global ans
    if value>=M:
        if value==M:
            ans=min(ans,count)
        return

    for co in coin:
        recur(value+co,count+1)

recur(0,0)
print(ans)



