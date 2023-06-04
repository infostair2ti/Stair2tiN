from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz

def count_days_weekday(date1,date2):
    result = {'0': 0,'1':0,'2': 0,'3':0,'4': 0,'5':0,'6':0}
    date_temp = date1
    while date_temp <= date2:
        weekday = date_temp.weekday() 
        result[str(weekday)] += 1        
        date_temp = date_temp+ relativedelta(days=1)
    return result
def get_label(count_days):
    result = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    return result.get(int(count_days),"")

def diference_two_dates(date1,date2):
    return (date2-date1)

def working_hours(date1,date2,holidays):
    date_tmp = date1
    days = 0
    while date_tmp <= date2:
        if date_tmp.date()  not in holidays:
            days+=1 
        date_tmp += relativedelta(days=1)
    return days

if __name__ == "__main__":
    print("Point C")
    date1 = datetime(2023,12,23)
    date2 = datetime(2024,1,2)
    print("Weekday Count Days")
    result = count_days_weekday(date1,date2)
    for weekday in result.keys():
        print("%s : %s"%(get_label(weekday),result[weekday]))
    print("----------------------------")
    print("Work Numbers")
    holidays = [
        datetime.strptime("01/01/2023", "%d/%m/%Y").date(),
        datetime.strptime("25/12/2023", "%d/%m/%Y").date(),
    ]
    hours = working_hours(date1,date2,holidays)
    print("hours: ",hours)
    print("----------------------------")
    print("Diference Date")
    diference_date = diference_two_dates(date1,date2)
    print("Seconds : ",diference_date.seconds)
    print("Hours : ",diference_date.total_seconds()/3600)
    print("Days : ",diference_date.days)
    print("----------------------------")
    print("Diference Date Distinct Zone")
    timezone = pytz.timezone('America/New_York')
    new_timezone = pytz.timezone('Asia/Tokyo')
    date3 = datetime(2023,2,6,tzinfo=timezone)
    date4 = datetime(2023,6,2,tzinfo=new_timezone)
    diference_date2 = diference_two_dates(date3,date4)
    print("Seconds : ",diference_date2.seconds)
    print("Hours : ",diference_date2.total_seconds()/3600)
    print("Days : ",diference_date2.days)
