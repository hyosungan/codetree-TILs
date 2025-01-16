n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

x=[i for i in range((ranges[0][1]))]

for i,(a,b) in enumerate(ranges):
    for j in x[:]:  #remove를 하면 인덱스를 이상하게 참조하기에 복사본을 사용 
        if j*(2**(i+1))>=a and j*(2**(i+1))<=b:
            pass
        else:
            x.remove(j)


print(x[0])
