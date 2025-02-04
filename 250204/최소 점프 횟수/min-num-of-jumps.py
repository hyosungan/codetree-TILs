def min_jumps(arr, pos=0, count=0, memo=None):
    if memo is None:
        memo = {}
    
    n = len(arr)
    if pos >= n - 1:
        return count  # 목적지 도착 시 현재 점프 횟수 반환
    if arr[pos] == 0:
        return float('inf')  # 점프 불가능한 경우 큰 값 반환
    
    # 메모이제이션 (이미 방문한 위치)
    if pos in memo and memo[pos] <= count:
        return float('inf')
    memo[pos] = count
    
    min_count = float('inf')
    
    for step in range(1, arr[pos] + 1):  # 1부터 arr[pos]까지 점프 가능
        min_count = min(min_count, min_jumps(arr, pos + step, count + 1, memo))
    
    return min_count

# 입력 처리
n = int(input().strip())
arr = list(map(int, input().strip().split()))

result = min_jumps(arr)
print(result if result != float('inf') else -1)
