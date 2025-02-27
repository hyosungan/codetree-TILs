n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic=dict()
for elem in arr:
    if elem in dic:
        dic[elem]+=1
    else:
        dic[elem]=1

sorted_dict = dict(sorted(dic.items(), key=lambda item: (-item[1],-item[0])))

for index,key in enumerate(sorted_dict.keys(),start=1):
    print(key,end=" ")
    if index==k:
        break