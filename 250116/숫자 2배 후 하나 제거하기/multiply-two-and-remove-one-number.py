import sys
INT_MAX=sys.maxsize
ans=INT_MAX

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    arr[i]*=2
    for j in range(n):
        left_arr=[]
        for k in range(n):
            if j!=k:
                left_arr.append(arr[k])

        diff=0
        for k in range(n-2):
            diff+=abs(left_arr[k+1]-left_arr[k])

        ans=min(ans,diff)

    arr[i]//=2

print(ans)

    
            