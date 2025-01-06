class Number:
    def __init__(self,num,idx):
        self.num=num
        self.idx=idx


N=int(input())
ans=[0]*(N)
arr=[]
numbers=list(map(int,input().split()))

for idx,num in enumerate(numbers,start=1):
    arr.append(Number(num,idx))

arr.sort(key=lambda x:(x.num,x.idx))

for index,number in enumerate(arr):
    ans[number.idx-1]=index+1

for i in ans:
    print(i,end=" ")





