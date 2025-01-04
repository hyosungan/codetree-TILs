N = input()
num=0
for i in N:
    num=num*2+int(i)

num=num*17
arr=[]
while True:
    if num<2:
        arr.append(num)
        break
    arr.append(num%2)
    num//=2

for n in arr[::-1]:
    print(n,end="")