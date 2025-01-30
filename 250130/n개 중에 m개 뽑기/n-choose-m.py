N, M = map(int, input().split())
arr = []

def choose(n):
    if n == M + 1:
        print(*arr)
        return

    for i in range(1, N + 1):
        if i in arr:  # 중복 방지
            continue
        if len(arr) > 0 and i < arr[-1]:  # 오름차순 유지
            continue
        arr.append(i)
        choose(n + 1)
        arr.pop()

choose(1)