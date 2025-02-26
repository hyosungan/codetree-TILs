#수를 n개 선택했을떄 그 중에 젤 작은 값이 있을거다. 그러면 모든 경우의 수를 봐서 젤 작은 값끼리 비교했을때
# 젤 작은 값들 도토리 키재기 한다음에 그나마 젤 큰놈일 경우, 그 큰놈 값을 return 해라

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
numbers=[]
visited=[0]*n #방문한 열을 체크
ans=0
def recur(idx):
    global ans
    if idx==n:
        ans=max(ans,min(numbers))
        return
    for i in range(n): #각 행마다 열을 돌려봄
        if visited[i]==1: #다른행에서 이미 방문한 열이라면 넘어감 
            continue
        visited[i]=1
        numbers.append(grid[idx][i])
        recur(idx+1)
        visited[i]=0
        numbers.pop()


recur(0) #첫번째 행 부터 시작

print(ans)

