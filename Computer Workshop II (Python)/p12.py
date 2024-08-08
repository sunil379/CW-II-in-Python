import datetime
def print_next_five_days():
    today = datetime.date.today()
    for i in range(5):
        next_day = today + datetime.timedelta(days=i)
        print(next_day.strftime("%A, %B %d, %Y"))
print_next_five_days()
