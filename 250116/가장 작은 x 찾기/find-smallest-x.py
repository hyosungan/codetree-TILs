n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

x=[i for i in range((ranges[0][1]//2))]

for i,(a,b) in enumerate(ranges):
    for j in x:
        if j*(2**(i+1))>=a and j*(2**(i+1))<=b:
            pass
        else:
            x.remove(j)


print(x[0])



