n=int(input())
a=set()
for _ in range(n):
    command=input().split()
    target=int(command[1])
    kind=command[0]

    if kind=='find':
        if target in a:
            print("true")
        else:
            print("false") 
    elif kind=='add':
        a.add(target)
    else:
        a.remove(target)

