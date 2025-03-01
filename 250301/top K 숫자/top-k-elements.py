from sortedcontainers import SortedSet

n,k=map(int,input().split())

arr=list(map(int,input().split()))

s=SortedSet(arr)

for i in s[len(s)-1:len(s)-k-1:-1]:
    print(i,end=' ')



