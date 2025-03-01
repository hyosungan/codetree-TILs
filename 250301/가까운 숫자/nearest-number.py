from sortedcontainers import SortedSet
import sys

n = int(input())
queries = list(map(int, input().split()))
s=SortedSet([0])

closest=sys.maxsize
for i in queries:
    s.add(i)
    right=s.bisect_right(i)
    if right!=len(s):
        candidate1=s[right]-i
    else:
        candidate1=sys.maxsize
    left=s.bisect_right(i)-2
    if left>=0:
        candidate2=i-s[left]
    else:
        candidate2=sys.maxsize
    closest=min(closest,candidate1,candidate2)
    print(closest)


