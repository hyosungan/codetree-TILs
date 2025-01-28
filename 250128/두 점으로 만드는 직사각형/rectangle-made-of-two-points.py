x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

a=min(x1,a1)
b=min(y1,b1)
c=max(x2,a2)
d=max(y2,b2)

print((c-a)*(d-b))