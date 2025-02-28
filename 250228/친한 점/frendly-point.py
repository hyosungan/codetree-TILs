from sortedcontainers import SortedSet

n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]
s=SortedSet(points)

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

for elem in queries:
    if s.bisect_left(elem)==len(s):
        print(-1,-1)
    else:
        point=s[s.bisect_left(elem)]
        x,y=point
        print(x,y)

