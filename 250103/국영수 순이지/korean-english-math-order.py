class Grade:
    def __init__(self, name,kor,math, eng):
        self.name=name
        self.kor=kor
        self.math=math
        self.eng=eng
grades=[]
n = int(input())

for _ in range(n):
    name,kor,math,eng = input().split()
    grades.append(Grade(name,int(kor),int(math),int(eng)))

grades.sort(key=lambda x: (-x.kor,-x.math,-x.eng))
for i in grades:
    print(i.name, i.kor, i.math, i.eng)
    
