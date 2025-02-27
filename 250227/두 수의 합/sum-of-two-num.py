n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic={}

for idx,elem in enumerate(arr):
    if elem in dic:
        dic[elem]+=1
    else:
        dic[elem]=1
ans=0
for i in arr:
    if k-i in dic:
        if i==k-i:
            ans+=dic[i]-1
        else:
            ans+=dic[k-i]
ans=ans//2
print(ans)
