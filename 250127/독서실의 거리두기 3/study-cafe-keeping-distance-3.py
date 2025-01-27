N = int(input())
seats = input()
arr=[int(char) for char in seats]

far=0
start=0
end=0

for i in range(N):
    for j in range(i+1,N):
        if arr[i]==1 and arr[j]==1:
            if far<j-i:
                far=j-i
                start=i
                end=j
            break
 
arr[int(end-start)//2]=1


ans=N
for i in range(N):
    for j in range(i+1,N):
        if arr[i]==1 and arr[j]==1:
            if ans>j-i:
                ans=j-i
            break
    
print(ans)

