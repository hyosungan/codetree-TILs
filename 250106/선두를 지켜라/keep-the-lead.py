n, m = map(int, input().split())

a=[]
b=[]
a_now=0
b_now=0
first=[]

for _ in range(n):
    v_a, t_a = map(int, input().split())
    for _ in range(int(t_a)):
        a_now=a_now+v_a
        a.append(a_now)
    

for _ in range(m):
    v_b, t_b = map(int, input().split())
    for _ in range(int(t_b)):
        b_now=b_now+v_b
        b.append(b_now)

for i,j in zip(a,b):
    if i>j:
        first.append('a')
    elif i<j:
        first.append('b')
    
answer=0
for i in range(1,len(first)):
    if first[i]!=first[i-1]:
        answer+=1

print(answer)
    

    


