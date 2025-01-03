secret_code, meeting_point, time = input().split()
time = int(time)

class exam:
    def __init__(self,s,m,t):
        self.secret_code=s
        self.meeting_point=m
        self.time=t

exam1=exam(secret_code,meeting_point,time)

print("secret code :",exam1.secret_code)
print("meeting point :",exam1.meeting_point)
print("time :",exam1.time)