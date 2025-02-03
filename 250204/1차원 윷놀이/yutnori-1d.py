n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
player=[1 for _ in range(k)]
ans=-1
#n번 만큼 재귀 돌리면서 

def choose(idx):
    global ans
    if idx==n:
        count=0
        for elem in player:
            if elem>=m:
                count+=1
        ans=max(ans,count)
        return
    for i in range(k):
        player[i]+=nums[idx]
        choose(idx+1)
        player[i]-=nums[idx]




choose(0)
print(ans)