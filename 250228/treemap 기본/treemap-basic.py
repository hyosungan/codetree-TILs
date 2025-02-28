from sortedcontainers import SortedDict

n = int(input())
dic=SortedDict()

for _ in range(n):
    line = input().split()
    if line[0]=='add':
        dic[int(line[1])]=int(line[2])
    elif line[0]=='find':
        if int(line[1]) in dic:
            print(dic[int(line[1])])
        else:
            print('None')
    elif line[0]=='remove':
        dic.pop(int(line[1]))
    else:
        if not dic:
            print('None')
        else:
            for val in dic.values():
                print(val,end=' ')
            print()



