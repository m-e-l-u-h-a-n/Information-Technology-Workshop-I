import datetime
import random
starting_date=datetime.date(2016,1,1)
ending_date=datetime.date(2018,3,23)
total_time=ending_date-starting_date
total_days=total_time.days
random_day=random.randrange(total_days)
random_date=starting_date+datetime.timedelta(days=random_day)
print('Random Date= ',random_date.strftime('%d-%m-%Y'))