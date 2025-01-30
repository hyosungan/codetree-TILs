K, N = map(int, input().split())
arr=[]
def choose(n):
    if n==N+1:
        for i in arr:
            print(i,end=" ")
        print()   
        return

    for i in range(1,K+1):
        if len(arr)>=2 and arr[-1]==i and arr[-2]==i:
            continue
        arr.append(i)
        choose(n+1)
        arr.pop()
    return
choose(1)