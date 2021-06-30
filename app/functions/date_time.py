# import module
import datetime


# Check time format
def check_time_format(send_time):
    is_valid = False
    try:
        datetime.datetime.strptime(send_time, "%H:%M")
    except ValueError as e:
        is_valid = False
    else:
        if datetime.datetime.strptime(send_time, "%H:%M"):
            is_valid = True
    return is_valid


# Check date format
def check_date_format(send_date):
    is_valid = False
    try:
        datetime.datetime.strptime(send_date, "%d/%m/%Y")
    except ValueError as e:
        is_valid = False
    else:
        if datetime.datetime.strptime(send_date, "%d/%m/%Y"):
            is_valid = True
    return is_valid


# get Today's Date
def get_todays_date():
    return datetime.date.today().strftime("%d/%m/%Y")


# get the time NOW
def get_time_now():
    return datetime.datetime.now().strftime("%H:%M")


# Check date given has not passed
def check_date_not_passed(today_date, send_date):
    today_date = datetime.datetime.strptime(today_date, "%d/%m/%Y")
    send_date = datetime.datetime.strptime(send_date, "%d/%m/%Y")
    if today_date <= send_date:
        return True
    else:
        return False


# Check time given has not passed
def check_date_time_not_passed(date_time_now, send_date_time):
    date_time_now = datetime.datetime.strptime(date_time_now, "%d/%m/%Y %H:%M")
    send_date_time = datetime.datetime.strptime(send_date_time, "%d/%m/%Y %H:%M")
    if date_time_now <= send_date_time:
        return True
    else:
        return False
