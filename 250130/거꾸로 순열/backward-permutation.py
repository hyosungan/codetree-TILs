n = int(input())

arr=[]
visited=[False]*(n+1)

def print_all():
    for i in arr:
        print(i,end=' ')
    print()
    
def choose(idx):
    if idx==n:
        print_all()
        return

    for i in range(n,0,-1):
        if visited[i]==False:
            arr.append(i)
            visited[i]=True
            choose(idx+1)
            arr.pop()
            visited[i]=False


choose(0)