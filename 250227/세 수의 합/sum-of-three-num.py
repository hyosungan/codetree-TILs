n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
count = dict()

for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1
ans = 0
for i in range(n):  #j<i<k 인 경우를 세줌 count에 남은 개수는 k의 후보 개수임
    count[arr[i]] -= 1
    for j in range(i):
        diff = k - arr[i] - arr[j]
        if diff in count:
            ans += count[diff]
            
print(ans)
