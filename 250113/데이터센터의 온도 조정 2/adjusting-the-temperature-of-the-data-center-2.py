N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

maxsize=0

def Range(temperature,a,b):
    work=0
    if temperature<a:
        work+=C
    elif temperature>=a and b>=temperature:
        work+=G
    else:
        work+=H
    return work


for temperature in range(-3,1001):
    sum_work=0
    for a,b in ranges:
        sum_work+=Range(temperature,a,b)
    maxsize=max(maxsize,sum_work)

print(maxsize)
    


     
