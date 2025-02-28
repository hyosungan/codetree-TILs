from sortedcontainers import SortedDict
#일반 dict와의 차이점은 key를 기준으로 자동 오름차순 정렬 된다는점이다. 
#나머지는 같음. 다만 시간복잡도만 O(logn)이됨

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



