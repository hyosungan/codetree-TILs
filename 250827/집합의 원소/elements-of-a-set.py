n, m = map(int, input().split())

uf=[i for i in range(n+1)]

def find(x):
    if uf[x]==x:
        return x
    root=find(uf[x])
    uf[x]=root
    return root


def union(a,b):
    A=find(a)
    B=find(b)
    uf[A]=B


for i in range(m):
    t,a,b=map(int,input().split())
    if t==0:
        union(a,b)
    else:
        if uf[a]==uf[b]:
            print("1")
        else:
            print("0")

