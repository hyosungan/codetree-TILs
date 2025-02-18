import sys
INT_MIN=-sys.maxsize

n = int(input())
arr = list(map(int, input().split()))


#처음부터 차례대로 최선의 선택을 해왔기 때문에 dp[i] 입장에서는 앞에 있던 최선의 선택을 가져갈 건지,
#아니면 뒤엎고 지 부터 시작할껀지만 고르면됨. 
#이렇게 골랐을때 dp[i]보다 dp[i-1]의 값이 높을수 있음
#왜냐하면 dp[i]는 a[i]를 반드시 포함하는 경우이기 때문 a[i]를 포함안한 전단계가 더 클수 있는거임

dp=[INT_MIN for _ in range(n)]

dp[0]=arr[0]

for i in range(1,n):
    dp[i]=max(dp[i-1]+arr[i],arr[i])

print(max(dp))