from sortedcontainers import SortedSet

n, m = map(int, input().split())
queries = list(map(int, input().split()))
s=SortedSet([i for i in range(1,m+1)])

for i in queries:
    s.remove(i)
    print(s[-1])




