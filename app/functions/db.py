# has all functions that relate to the db
import sqlite3


# connecting to the database
def sqlite_connect():
    db_file = "/home/maina-muriuki/Documents/python_whatsapp_scheduler/app/db/whatsapp_scheduler.db"
    try:
        sqlite_connection = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        return "Error! Failed to connect to db"

    return sqlite_connection


# create table
def create_table(sqlite_connection):
    try:
        cursor = sqlite_connection.cursor()

        cursor.execute('''CREATE TABLE messages(
                        id integer PRIMARY KEY AUTOINCREMENT,
                        date_time_scheduled varchar(20) NOT NULL,
                        message varchar(20) NOT NULL,
                        recipient_number varchar(25),
                        date_time_sent)''')

        print("Successfully created table")
    except sqlite3.Error as error:
        print("Error while creating table")
        created_table = False
    else:
        created_table = True
    return created_table


def insert_data(sqlite_connection, data):
    try:
        cursor = sqlite_connection.cursor()
        # Insert a row of data into messages table
        cursor.execute(
            f'INSERT INTO messages (date_time_scheduled,message,recipient_number,date_time_sent) VALUES ("{data[0]}","{data[1]}","{data[2]}","{data[3]}")')
        if sqlite_connection.commit():
            return True
    except sqlite3.Error as error:
        print("Error while inserting data")
        return False


def select_data(sqlite_connection):
    # Query all rows in the stocks table
    try:
        cursor = sqlite_connection.cursor()
        messages = cursor.execute('''SELECT * FROM messages''').fetchall()
        if len(messages) > 0:
            print("Messages stored: \n")
            for row in messages:
                print(row)
        else:
            print("No messages stored yet")

    except sqlite3.Error as error:
        print("Error while selecting data", error)
