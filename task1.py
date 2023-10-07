from datetime import datetime
from collections import defaultdict

MAX_DELTA_DAYS = 7
CURRENT_DATE = datetime.today().date() #datetime(year=2023, month=12, day=30).date() 
WEEKDAYS_LIST = [datetime(year=2001, month=1, day=i).strftime('%A') for i in range(1,8)]

def get_birthdays_per_week(users: list) -> list:
    user_bd_by_weekday = defaultdict(list)
    #CURRENT_DATE = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date() 
        birthday_this_year = birthday.replace(year=CURRENT_DATE.year)
        
        today_distance = (birthday_this_year - CURRENT_DATE).days
        #let's not forget about those who had birthday on weekend and today is Monday
        if today_distance < 0:
            today_distance = (birthday_this_year.replace(year=CURRENT_DATE.year + 1) - CURRENT_DATE).days
            if today_distance > MAX_DELTA_DAYS:
                continue
        
        if today_distance > MAX_DELTA_DAYS:
            continue
        
        bd_week_day = birthday_this_year.weekday()
        
        if (bd_week_day == 5 and today_distance < MAX_DELTA_DAYS - 2) or (bd_week_day == 6 and today_distance < MAX_DELTA_DAYS - 1):
            bd_week_day = 0
            
        bd_week_day_name = WEEKDAYS_LIST[bd_week_day]
        
        user_bd_by_weekday[bd_week_day_name].append(name)


    print(''.join(['{}: {}\n'.format(d, user_bd_by_weekday[d]) for d in user_bd_by_weekday if len(user_bd_by_weekday[d]) > 0]))
    
            
#get_birthdays_per_week([{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}
#                        , {"name": "test", "birthday": datetime(1955, 10, 6)}
#                        , {"name": "test2", "birthday": datetime(1955, 10, 8)}
#                        , {"name": "test3", "birthday": datetime(1955, 10, 10)}
#                        , {"name": "test4", "birthday": datetime(1955, 10, 7)}])
#
#get_birthdays_per_week([{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}
#                        , {"name": "test", "birthday": datetime(1955, 12, 29)}
#                        , {"name": "test2", "birthday": datetime(1955, 12, 31)}
#                        , {"name": "test3", "birthday": datetime(1955, 1, 1)}
#                        , {"name": "test4", "birthday": datetime(1955, 1, 7)}
#                        , {"name": "test5", "birthday": datetime(1955, 1, 6)}])