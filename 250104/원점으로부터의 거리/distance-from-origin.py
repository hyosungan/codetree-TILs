class Point:
    def __init__(self, x,y,number):
        self.x=x
        self.y=y
        self.number=number

n = int(input())
points=[]

for i in range(1,n+1):
    x,y=tuple(map(int,input().split()))
    points.append(Point(x,y,i))

points.sort(key=lambda X: (abs(X.x)+abs(X.y),X.number))

for point in points:
    print(point.number)



