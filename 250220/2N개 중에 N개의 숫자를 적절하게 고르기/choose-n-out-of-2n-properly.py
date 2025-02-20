import sys
INT_MAX=sys.maxsize
n = int(input())
A = list(map(int, input().split()))

total=sum(A)
ans=INT_MAX
def recur(idx,select,count):
    global ans
    if select>n:
        return
    if idx==2*n:
        if select==n:
            ans=min(ans,abs(total-2*count))
        return
    recur(idx+1,select+1,count+A[idx])
    recur(idx+1,select,count)


recur(0,0,0)

print(ans)