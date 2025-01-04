m1, d1, m2, d2 = map(int, input().split())
day1=0
day2=0
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(m1):
    day1+=days[i]
day1+=d1

for i in range(m2):
    day2+=days[i]
day2+=d2

print(day2-day1+1)