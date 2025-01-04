class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

n = int(input())

students= []


for _ in range(n):
    name,sub1,sub2,sub3 = input().split()
    students.append(Student(name,int(sub1),int(sub2),int(sub3)))

students.sort(key=lambda x: x.sub1 + x.sub2 + x.sub3)

for i in students:
    print(i.name, i.sub1, i.sub2, i.sub3)
    
