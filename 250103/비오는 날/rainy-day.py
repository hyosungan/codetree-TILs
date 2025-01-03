class Forecast:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather

forecasts=[]
n = int(input())

for _ in range(n):
    d, dy, w = input().split()
    forecasts.append(Forecast(d,dy,w))

earliest='2100-12-31'
earliest_day=''
for i in range(len(forecasts)):
    if forecasts[i].weather=='Rain':
        date_info=forecasts[i].date.split('-')
        if date_info[0]<earliest.split('-')[0]:
            earliest=forecasts[i].date
            earliest_day=forecasts[i].day
        elif date_info[0]==earliest.split('-')[0]:
            if date_info[1]<earliest.split('-')[1]:
                earliest=forecasts[i].date
                earliest_day=forecasts[i].day
            elif date_info[1]==earliest.split('-')[1]:
                if date_info[2]<earliest.split('-')[2]:
                    earliest=forecasts[i].date
                    earliest_day=forecasts[i].day
                elif date_info[2]==earliest.split('-')[2]:
                    earliest=forecasts[i].date
                    earliest_day=forecasts[i].day
print(earliest,earliest_day,'Rain')


