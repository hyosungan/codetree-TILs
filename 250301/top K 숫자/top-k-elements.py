from sortedcontainers import SortedSet

n,k=map(int,input().split())

arr=list(map(int,input().split()))

s=SortedSet(arr)

ss=list(s)

ss.sort(reverse=True)
for i in ss[:k]:
    print(i,end=' ')



