import os
from functions import check_numbers, date_time, db, whatsapp_send_message

db_file = os.path.dirname(os.path.abspath(__file__)) + "/db/whatsapp_scheduler.db"

# function to create sqlite table
def create_db_tables():
    db_connection = db.sqlite_connect(db_file)
    table_created = db.create_tables(db_connection)
    db_connection.close()
    return table_created


# select all messages in the db
def select_all_messages():
    db_connection = db.sqlite_connect(db_file)
    messages = db.select_messages(db_connection)
    db_connection.close()
    return messages


# select all contacts in the db
def select_contacts():
    db_connection = db.sqlite_connect(db_file)
    contacts = db.select_numbers(db_connection)
    db_connection.close()
    return contacts


# select a single contact from the db
def select_contact(name):
    db_connection = db.sqlite_connect(db_file)
    contact = db.select_number(db_connection, name)
    db_connection.close()
    return contact


# insert message into db
def insert_messages(data):
    db_connection = db.sqlite_connect(db_file)
    inserted_data = db.insert_messages(db_connection, data)
    db_connection.close()
    return inserted_data


# insert phonenumbers into db
def insert_contacts(data):
    db_connection = db.sqlite_connect(db_file)
    inserted_data = db.insert_contacts(db_connection, data)
    db_connection.close()
    return inserted_data


# user inputs how many phonenumbers they want to send the message to
def input_number_phonenumbers():
    number_of_phonenumbers = input("How many numbers do you want to send the message to:\n 1. One \n 2. Multiple\n")
    # Ensure choice is valid
    is_valid_choice = check_numbers.check_options(number_of_phonenumbers)
    # if choice is invalid loop till choice is valid
    while not is_valid_choice:
        number_of_phonenumbers = input(
            "Invalid Choice! How many numbers do you want to send the message to:\n 1. One \n 2. Multiple\n")
        is_valid_choice = check_numbers.check_options(number_of_phonenumbers)

    return number_of_phonenumbers


def get_phonenumber():
    phonenumber = input("Enter recipient's number(International format e.g +254**********): +")

    # validate recipient's number
    is_valid_number = check_numbers.check_phone_number(phonenumber)

    # Loop to request for correct number format in case of validation
    while not is_valid_number:
        phonenumber = input("Invalid Number! Please try again. Enter recipient's number: +")
        is_valid_number = check_numbers.check_phone_number(phonenumber)
    return phonenumber


def save_number(recipients_number):
    contacts = select_contacts()
    save_numbers = input("Do you want to save the list:\n 1. Yes \n 2. No\n")
    is_valid_choice = check_numbers.check_options(save_numbers)
    while not is_valid_choice:
        save_numbers = input(
            "Invalid Choice! Please select \"1\" or \"2\" \nWDo you want to save the list:\n 1. Yes \n "
            "2. No\n")
        is_valid_choice = check_numbers.check_options(save_numbers)
    if save_numbers == "1" and is_valid_choice == True:
        stored_names = []
        for contact in contacts:
            stored_names.append(contact[1])
        print("Currently saved(Not available):", stored_names)
        name = input("Please enter a unique name for the contact list: ")
        is_valid_name = any(name for n in contacts if n[1] == name)
        while is_valid_name:
            name = input("Please enter a unique name for the contact list: ")
            is_valid_name = any(name for n in contacts if n[1] == name)
        print("Successfully saved contact list: ", name)
        if not is_valid_name:
            contact_list = [name, str(recipients_number)]
            return insert_contacts(contact_list)


# user prompted to input recipient's number
def input_phonenumber():
    # get number of phonenumbers choice
    number_of_phonenumbers = input_number_phonenumbers()
    recipients_number = []
    if number_of_phonenumbers == "1":
        phonenumber = get_phonenumber()
        # Add phonenumber to list
        recipients_number.append(phonenumber)
    elif number_of_phonenumbers == "2":
        where_get_numbers = input("Where do you want to get the numbers: \n 1. Select a saved contact list \n 2. "
                                  "Enter the recipient\'s numbers\n")
        is_valid_choice = check_numbers.check_options(where_get_numbers)
        # if choice is invalid loop till choice is valid
        while not is_valid_choice:
            where_get_numbers = input("Where do you want to get the numbers: \n 1. Select a saved contact list \n 2. "
                                      "Enter the recipient\'s numbers\n")
            is_valid_choice = check_numbers.check_options(where_get_numbers)

        if where_get_numbers == "1":
            contacts = select_contacts()
            if len(contacts) < 1:
                print("Whoops! You have no phonenumbers currently stored.")
                recipients_number = input_many_numbers()
                save_number(recipients_number)

            else:
                print("Saved Contacts:\n")
                n = 1
                for contact in contacts:
                    print(n, contact[1])
                    n += 1
                name = input("Please enter the name of the contact list you want to send the message: ")
                is_valid_name = any(name for n in contacts if n[1] == name)
                print(name for n in contacts if n.name == name)
                while not is_valid_name:
                    name = input("Invalid name! Please enter the name of the contact list you want to send the "
                                 "message: ")
                    is_valid_name = any(name for n in contacts if n[1] == name)
                contact_list = select_contact(name)
                recipients_number = contact_list[0][2]
                recipients_number = recipients_number.replace("'", "")
                recipients_number = recipients_number.strip('][').split(', ')
        elif where_get_numbers == "2":
            recipients_number = input_many_numbers()
            save_number(recipients_number)

    return recipients_number


# input multiple numbers
def input_many_numbers():
    recipients_numbers = []
    phonenumber = '0'
    print("ATTENTION! When done entering numbers add number \'done\'")
    while phonenumber != "done":
        if phonenumber == "done" and len(recipients_numbers) > 0:
            break
        else:
            phonenumber = get_phonenumber()
            if phonenumber != "done":
                recipients_numbers.append(phonenumber)

    return recipients_numbers


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
    return send_time + ":00"


# user prompted to input date to send message
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

    # send to recipients

    # recipient's number
    recipients_numbers = input_phonenumber()

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
    for phonenumber in recipients_numbers:
        if whatsapp_send_message.send_message(message, phonenumber):
            data = [date_time_now, message, phonenumber, send_date_time]
            insert_messages(data)


if __name__ == "__main__":
    main()
    print("Messages stored: \n")
    messages = select_all_messages()
    for row in messages:
        print(row)
