from sortedcontainers import SortedSet

T = int(input())
s=SortedSet()

for _ in range(T):
    k = int(input())
    for i in range(k):
        command=input().split()
        kind=command[0]
        num=int(command[1])
        if kind=='I':
            s.add(num)
        elif kind=='D':
            if num==1:
                if s:
                    s.remove(s[-1])
            elif num==-1:
                if s:
                    s.remove(s[0])
    if not s:
        print("EMPTY")
    else:
        print(s[-1],s[0])

 