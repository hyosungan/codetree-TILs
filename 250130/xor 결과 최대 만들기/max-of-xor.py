n, m = map(int, input().split())
A = list(map(int, input().split()))
arr=[]
ans=-1



def xor():
    global ans
    xor=0
    for i in range(m):
        xor=xor^arr[i]
    ans=max(ans,xor)


def choose(idx,cnt):
    if idx==n:
        if cnt==m:
            xor()
        return
    #넣을래
    arr.append(A[idx])
    choose(idx+1,cnt+1)
    arr.pop()

    #안넣을래
    choose(idx+1,cnt)
    

choose(0,0)

print(ans)