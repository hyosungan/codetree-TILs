import heapq

# 변수 선언 및 입력:
n = int(input())
pq = []

for _ in range(n):
    x = int(input())

    # x가 0이 아니라면
    # 우선순위 큐에 넣어줍니다.
    # 단, 절댓값이 작은 값부터 나오도록
    # (|x|, x) 형태로 넣어줍니다.
    if x != 0:
        heapq.heappush(pq, (abs(x), x))
    # x가 0이라면
    # 가장 앞에 있는 원소를 출력해주고 제거합니다.
    else:
        # 우선순위 큐가 비어져 있다면 0을 출력하고 넘어갑니다.
        if not pq:
            print(0)
            continue
        _, v = heapq.heappop(pq)
        print(v)




        



