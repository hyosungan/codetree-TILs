a, b, x, y = map(int, input().split())

case1=abs(b-a)

case2=abs(a-x)+abs(y-b)

case3=abs(a-y)+abs(x-b)

print(min(case1,case2,case3))