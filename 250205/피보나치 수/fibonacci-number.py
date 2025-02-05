N = int(input())
dp=[-1]*100
def fibo(n):
    if dp[n]!=-1:
        return dp[n]
    if n<=2:
        return 1
    else:
        dp[n]=fibo(n-1)+fibo(n-2)
        return dp[n]

print(fibo(N))
