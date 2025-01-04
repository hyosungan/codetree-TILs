class Student:
    def __init__(self, height,weight,number):
        self.height=height
        self.weight=weight
        self.number=number

students=[]
n = int(input())

for i in range(1,n+1):
    h,w=input().split()
    students.append(Student(int(h),int(w),i))

students.sort(key=lambda x: (-x.height,-x.weight,x.number))

for x in students:
    print(x.height,x.weight,x.number)
    



