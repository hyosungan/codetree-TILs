import sys
INT_MAX=sys.maxsize

n, m = map(int, input().split())
coin = list(map(int, input().split()))
dp=[INT_MAX for _ in range(m+1)]
dp[0]=0

for i in range(n): #동전 하나씩 해봄
    for j in range(m,0,-1):
    #목표 수부터 차례대로 내려오면서 dp를 채움. 
    #이렇게 하면 하나의 수는 1번만 쓸수 있음
    #왜냐하면 해당 동전을 합하기전에 값이 있었는지 보는데 
    #첫번째 for 문에서 동전 1개씩 돌려보기 때문에 1개 보다 많아 쓰는 경우는 없음
        if j<coin[i]: #수가 코인보다 작은 수면 볼 필요도 없음 #이거 해야 뒤에 [j-coin[i]]인덱스 범위 오류 안남
            continue 
        if dp[j-coin[i]]==INT_MAX:  #코인 더하기 전의 수가 불가능한 경우라면 패스
            continue
        dp[j]=min(dp[j-coin[i]]+1,dp[j])
if dp[m]==INT_MAX:
    print(-1)
else:
    print(dp[m])