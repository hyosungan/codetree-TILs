n = int(input())
arr=[]
A=0
B=0
stage='O'
ans=0
for _ in range(n):
    ci, si = input().split()
    arr.append((ci,int(si)))

for user,value in arr:
    if user=='A':
        A+=value
    if user=='B':
        B+=value
    if A>B:
        if stage!='A':
            ans+=1
            stage='A'
    elif A<B:
        if stage!='B':
            ans+=1
            stage='B'
    else:
        if stage!='AB':
            ans+=1
            stage='AB'

print(ans)