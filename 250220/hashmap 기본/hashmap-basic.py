n = int(input())
commands = []
d={}
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

for com in commands:
    if com[0]=='add':
        d[com[1]]=com[2]
    elif com[0]=='remove':
        d.pop(com[1])
    else:
        if com[1] in d:
            print(d[com[1]])
        else:
            print('None')
