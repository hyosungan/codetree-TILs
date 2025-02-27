n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic={}

for idx,elem in enumerate(arr):
    if elem in dic:
        dic[elem]+=1
    else:
        dic[elem]=1
ans=0
for i in range(n):
    if ((k-arr[i] in dic) and (dic[k-arr[i]]>0)) and ((arr[i] in dic) and (dic[arr[i]]>0)):
        ans+=1
        dic[k-arr[i]]-=1
        dic[arr[i]]-=1

print(ans)
