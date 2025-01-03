class Person:
    def __init__(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight

persons=[]
n = int(input())

for _ in range(n):
    n_i, h_i, w_i = input().split()
    persons.append(Person(n_i,h_i,w_i))

persons.sort(key=lambda x: x.height)

for i in persons:
    print(i.name, i.height,i.weight)

