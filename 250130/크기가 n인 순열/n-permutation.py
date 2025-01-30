N= int(input())
arr=[]
visited=[False]*(N+1)
#1번째 자리부터 N번째 자리까지 각자리 마다 for문을 돌리는데, 만약 방문한 적이 있는 숫자라면 continue로 넘어감.
def print_all():
    for i in arr:
        print(i,end=' ')
    print()


def choose(n):
    if n==N+1:
        print_all()
        return

    for i in range(1,N+1):
        if visited[i]==True:
            continue
        arr.append(i)
        visited[i]=True
        choose(n+1)
        arr.pop()
        visited[i]=False



choose(1)