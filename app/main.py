from functions import check_numbers, date_time, db,whatsapp_send_message


# function to create sqlite table
def create_db_table():
    db_connection = db.sqlite_connect()
    table_created = db.create_table(db_connection)
    db_connection.close
    return table_created

# select all messages in the db
def select_all_messages():
    db_connection = db.sqlite_connect()
    db.select_data(db_connection)
    db_connection.close()

# insert data into db
def insert_data(data):
    db_connection = db.sqlite_connect()
    inserted_data = db.insert_data(db_connection,data)
    db_connection.close
    return inserted_data

# user prompted to input recipient's number
def input_number():
    recipient_number = input("Enter recipient's number(International format e.g +254**********): +")

    # validate recipient's number
    is_valid_number = check_numbers.check_phone_number(recipient_number)

    # Loop to request for correct number format in case of validation
    while not is_valid_number:
        recipient_number = input("Invalid Number! Please try again. Enter recipient's number: +")
        is_valid_number = check_numbers.check_phone_number(recipient_number)

    return recipient_number


# user prompted with options of date to send message
def input_when_option():
    when_date = input("What DATE do you want to send the message:\n 1. Today \n 2. Set a date\n")
    is_valid_choice = check_numbers.check_options(when_date)
    while not is_valid_choice:
        when_date = input("Invalid Choice! Please select \"1\" or \"2\" \nWhat DATE do you want to send the "
                          "message:\n 1. Today \n 2. Set a date\n")
        is_valid_choice = check_numbers.check_options(when_date)
    return when_date


# user prompted to input time to send message
def input_time():
    send_time = input("Please Enter the time to send message (Use 24-format e.g HH:MM): ")
    valid_time_format = date_time.check_time_format(send_time)
    while not valid_time_format:
        send_time = input("Invalid Time! Please Enter the time to send message (Use 24-format e.g HH:MM): ")
        valid_time_format = date_time.check_time_format(send_time)
    return send_time


# user promted to input date to send message
def input_date():
    send_date = input("Please Enter the date to send message (In the format e.g dd/mm/yyyy): ")
    valid_date_format = date_time.check_date_format(send_date)
    while not valid_date_format:
        send_date = input(
            "Invalid Date! Please Enter the date to send message (In the format e.g dd/mm/yyyy): ")
        valid_date_format = date_time.check_date_format(send_date)
    return send_date


def main():
    # message to send
    message = input("Enter message to send: ")

    # recipient's number
    recipient_number = input_number()

    # ask user whether to select option of when to send date
    when_date = input_when_option()

    if when_date == "1":
        # ask user to enter time
        send_time = input_time()
        date_time_now = date_time.get_todays_date() + " " + date_time.get_time_now()
        send_date_time = date_time.get_todays_date() + " " + send_time
        valid_time = date_time.check_date_time_not_passed(date_time_now, send_date_time)
        while not valid_time:
            print("ERROR! The time entered has already passed!")
            send_time = input_time()
            date_time_now = date_time.get_todays_date() + " " + date_time.get_time_now()
            send_date_time = date_time.get_todays_date() + " " + send_time
            valid_time = date_time.check_date_time_not_passed(date_time_now, send_date_time)


    elif when_date == "2":
        # user inputs date
        send_date = input_date()
        valid_date = date_time.check_date_not_passed(date_time.get_todays_date(), send_date)
        while not valid_date:
            print("ERROR! The date entered has already passed!")
            send_date = input_date()
            valid_date = date_time.check_date_not_passed(date_time.get_todays_date(), send_date)
        if valid_date:
            send_time = input_time()
            date_time_now = date_time.get_todays_date() + " " + date_time.get_time_now()
            send_date_time = send_date + " " + send_time
            valid_time = date_time.check_date_time_not_passed(date_time_now, send_date_time)
            while not valid_time:
                print("ERROR! The time  entered has already passed!")
                send_time = input_time()
                date_time_now = date_time.get_todays_date() + " " + date_time.get_time_now()
                send_date_time = send_date + " " + send_time
                valid_time = date_time.check_date_time_not_passed(date_time_now, send_date_time)

    date_time.countdown_timer(date_time_now, send_date_time)
    if whatsapp_send_message.send_message(message, recipient_number):
        data = [date_time_now, message, recipient_number, send_date_time]
        insert_data(data)


if __name__ == "__main__":
    main()
    select_all_messages()
