pos = list(map(int, input().split()))

pos.sort()

if pos[2]-pos[0]==2:
    print(0)
else:
    print(2)


