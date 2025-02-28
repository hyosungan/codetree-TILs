from sortedcontainers import SortedSet


n, m = map(int, input().split())
arr = list(map(int, input().split()))
s=SortedSet(arr)
queries = [int(input()) for _ in range(m)]

for elem in queries:
    if s.bisect_left(elem)==len(s):
        print(-1)
    else:
        print(s[s.bisect_left(elem)])
