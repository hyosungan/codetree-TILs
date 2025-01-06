N, M, K = map(int, input().split())
punish = [int(input()) for _ in range(M)]

arr=[0]*(N+1)

for i in punish:
    arr[i]+=1
    if arr[i]==K:
        print(i)
        break
    # for j in range(len(arr)):
    #     if arr[j]==K:
    #         print(j)
    #         break
    
else:
    print(-1)




