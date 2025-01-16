n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

x = 1  # 가능한 x의 최소값부터 시작

while True:
    valid = True
    current_value = x
    for a, b in ranges:
        if not (a <= current_value*2 <= b):
            valid = False
            break
        current_value *= 2  # 다음 단계로 값 업데이트
    
    if valid:
        print(x)
        break
    x += 1