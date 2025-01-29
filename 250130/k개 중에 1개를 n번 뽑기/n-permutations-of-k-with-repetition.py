K, N = map(int, input().split())
arr=[]
def print_num():
    for i in arr:
        print(i,end=' ')
    print()


def choose(n):
    if n==N+1:
        print_num()
        return

    for i in range(1,K+1):
        arr.append(i)
        choose(n+1)
        arr.pop()
    return

choose(1)


