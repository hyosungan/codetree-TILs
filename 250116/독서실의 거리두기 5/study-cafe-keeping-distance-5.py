N = int(input())
st = input()
seat=[int(i) for i in st]
ans=0
for index,element in enumerate(seat):   
    if element==1:
        continue

    else:
        seat[index]=1
        distance=N
        for i in range(N):  
            for j in range(i+1,N):
                if seat[i]==1 and seat[j]==1:
                    distance=min(distance,j-i)
                    break
        
        ans=max(distance,ans)

        seat[index]=0
print(ans)

    