import sys
INT_MIN=-sys.maxsize

N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

dp=[INT_MIN for _ in range(M+1)]
dp[0]=0

for i in range(1,M+1):
    for j in range(N):
        if i<w[j]:
            continue
        if dp[i-w[j]]==INT_MIN:
            continue
        dp[i]=max(dp[i],dp[i-w[j]]+v[j])

print(max(dp))

