A = input()
ans=0
for i in range(len(A)-1):
    if A[i:i+2]=='((':
        for j in range(i,len(A)-1):
            if A[j:j+2]=='))':
                ans+=1

print(ans)

