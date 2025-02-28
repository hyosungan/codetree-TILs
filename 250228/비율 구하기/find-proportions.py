from sortedcontainers import SortedDict

dic=SortedDict()

n = int(input())
words = [input() for _ in range(n)]

for elem in words:
    if elem in dic:
        dic[elem]+=1
    else:
        dic[elem]=1

for key,val in dic.items():
    print(f"{key} {val/n*100:.4f}")

