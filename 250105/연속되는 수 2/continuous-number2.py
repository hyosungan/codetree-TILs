n = int(input())
arr = [int(input()) for _ in range(n)]
max_num=0
count=0
for i in range(len(arr)):
    
    if i==0 or arr[i]!=arr[i-1]:
        count=1
    elif arr[i]==arr[i-1]:
        count+=1
        if max_num<count:
            max_num=count

print(max_num)
    
