n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans=100

def is_possible(max_num):
    posible_index=[]
    for idx,elem in enumerate(arr):
        if max_num>=elem:
            posible_index.append(idx)
    if (0 not in posible_index) or ((len(arr)-1) not in posible_index):
        return False
    
    for i in range(1,len(posible_index)):
        if posible_index[i]-posible_index[i-1]>k:
            return False
    return True

for i in range(1,max(arr)):
    if is_possible(i):
        ans=min(ans,i)

print(ans)


    