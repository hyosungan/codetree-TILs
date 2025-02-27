n, m = map(int, input().split())

words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]
dic={}

for idx,elem in enumerate(words[1:],start=1):
    dic[idx]=elem
    dic[elem]=idx

for i in queries:
    if i.isdigit():
        print(dic[int(i)])
    else:
        print(dic[i])
    
