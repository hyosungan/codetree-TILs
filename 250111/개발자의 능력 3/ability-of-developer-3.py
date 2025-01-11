import sys

INT_MAX=sys.maxsize
ans=INT_MAX

abilities = list(map(int, input().split()))
length=len(abilities)

def differ(i,j,k):
    team1=abilities[i]+abilities[j]+abilities[k]
    team2=sum(abilities)-team1
    return abs(team1-team2)

for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            ans=min(ans,differ(i,j,k))

print(ans)
            
