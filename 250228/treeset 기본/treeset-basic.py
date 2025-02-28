from sortedcontainers import SortedSet

s=SortedSet()
n = int(input())

for _ in range(n):
    command=input().split()
    kind=command[0]
    if kind=='add':
        s.add(command[1])
    elif kind=='remove':
        s.remove(command[1])
    elif kind=='find':
        print('true' if command[1] in s else 'false')
    elif kind=='lower_bound':
        print(s[s.bisect_left(command[1])] if s.bisect_left(command[1])<len(s) else None)

    elif kind=='upper_bound':
        print(s[s.bisect_right(command[1])] if s.bisect_right(command[1])<len(s) else None)
    elif kind=='largest':
        print(s[-1] if s else None)
    elif kind=='smallest':
        print(s[0] if s else None)

