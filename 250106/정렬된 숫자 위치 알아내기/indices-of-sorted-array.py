class Number:
    def __init__(self, num, idx=0):
        self.num=num
        self.idx=idx

arr=[]
N=int(input())

numbers=list(map(int,input().split()))

for number in numbers:
    arr.append(Number(number))

arr.sort(key=lambda x:x.num)

for index,number in enumerate(arr,start=1):
    number.idx=index
    

ans=[]
for i in numbers:
    for number in arr:
        if i==number.num:
            ans.append(number.idx)
            arr.remove(number)
            break
            

for i in ans:
    print(i,end=' ')





