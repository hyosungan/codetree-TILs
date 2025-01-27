pos = list(map(int, input().split()))

pos.sort()

if pos[2]-pos[0]==2:
    print(0)
# elif pos[2]-pos[0]==3:
#     print(1)
elif (pos[1]-pos[0])==2 or (pos[2]-pos[1])==2:
    print(1)
else:
    print(2)


