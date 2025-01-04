a, b, c = map(int, input().split())

minute=11*24*60+11*60+11

minute2=a*24*60+b*60+c

if minute2-minute<0:
    print(-1)

else:
    print(minute2-minute)

