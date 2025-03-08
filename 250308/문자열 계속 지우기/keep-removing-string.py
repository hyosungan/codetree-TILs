A = input()
B = input()
length=len(B)
while True:
    if B not in A:
        print(A)
        break

    for i in range(len(A)-length+1):
        if A[i:i+length]==B:
            A=A[:i]+A[i+length:]
            break