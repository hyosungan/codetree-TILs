n=int(input())

arr=[]
ans=0
#백트래킹으로 n자리의 모든 경우의 수들 돌면서
#만약 아름다운 수 라면 ans를 1씩 증가
#아름다운수는 1이든 2이든 나와있으면 그만큼 연속으로 나오는지 체크

def is_beautiful():
    begin=0

    while begin<n:

        if begin+arr[begin]-1>=n:
            return False

        for i in range(begin,begin+arr[begin]):
            if arr[i]!=arr[begin]:
                return False
        begin=begin+arr[begin]

    return True

        # if begin==len(arr):
        #     return True
        # if begin>len(arr):
        #     return False
        # if begin+arr[begin]>len(arr):
        #     return False
        
        

def P(idx):
    global ans
    if idx==n:
        if is_beautiful():
            ans+=1
        return 

    for i in range(1,5):
        arr.append(i)
        P(idx+1)
        arr.pop()

P(0)
print(ans)