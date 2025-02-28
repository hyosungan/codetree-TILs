from sortedcontainers import SortedDict

dic=SortedDict()

n=int(input())
arr=list(map(int,input().split()))

for idx,elem in enumerate(arr,start=1):
    if elem in dic:
        continue
    dic[elem]=idx

for key,value in dic.items():
    print(key,value)

