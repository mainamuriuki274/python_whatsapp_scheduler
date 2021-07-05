# has all functions that relate to the db
import sqlite3


# connecting to the database
def sqlite_connect(db_file):
    try:
        sqlite_connection = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        return "Error! Failed to connect to db"

    return sqlite_connection


# create table
def create_tables(sqlite_connection):
    try:
        cursor = sqlite_connection.cursor()

        cursor.execute('''CREATE TABLE messages(
                        id integer PRIMARY KEY AUTOINCREMENT,
                        date_time_scheduled varchar(20) NOT NULL,
                        message varchar(20) NOT NULL,
                        recipient_number varchar(25) NOT NULL,
                        date_time_sent varchar(25) NOT NULL)''')

        cursor.execute('''CREATE TABLE phonenumbers(
                                id integer PRIMARY KEY AUTOINCREMENT,
                                name varchar(20) NOT NULL UNIQUE,
                                phonenumbers text NOT NULL)''')

        cursor.close()
        print("Successfully created tables")
        return True
    except sqlite3.Error as error:
        print("Error while creating tables")
        return False


def insert_messages(sqlite_connection, data):
    try:
        cursor = sqlite_connection.cursor()
        # Insert a row of data into messages table
        if cursor.execute(
                'INSERT INTO messages (date_time_scheduled,message,recipient_number,date_time_sent) VALUES (?,?,?,?)',
                (data[0], data[1], data[2], data[3])):
            sqlite_connection.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Error while inserting data")
        return False


def select_messages(sqlite_connection):
    # Query all rows in the messages table
    try:
        cursor = sqlite_connection.cursor()
        messages = cursor.execute("SELECT * FROM messages").fetchall()
        if len(messages) > 0:
            cursor.close()
            return messages
        else:
            print("No messages stored yet")
            cursor.close()
            return []

    except sqlite3.Error as error:
        print("Error while selecting data")
        return False


# function to select all lines in db
def select_numbers(sqlite_connection):
    # Query all rows in the phonenumbers table
    try:
        cursor = sqlite_connection.cursor()
        contacts = cursor.execute("SELECT * FROM phonenumbers").fetchall()
        if len(contacts) > 0:
            cursor.close()
            return contacts
        else:
            cursor.close()
            return []

    except sqlite3.Error as error:
        print("Error while selecting data", error)
        return False


# function to select single line in db
def select_number(sqlite_connection, name):
    # Query all rows in the phonenumbers table
    try:
        cursor = sqlite_connection.cursor()
        contact = cursor.execute("SELECT * FROM phonenumbers WHERE name = '"+name+"'").fetchall()
        if len(contact) == 1:
            cursor.close()
            return contact
        else:
            cursor.close()
            return []

    except sqlite3.Error as error:
        print("Error while selecting data")
        return False


def insert_contacts(sqlite_connection, data):
    try:
        cursor = sqlite_connection.cursor()
        # Insert a row of data into messages table
        if cursor.execute(
                'INSERT INTO phonenumbers (name,phonenumbers) VALUES (?,?)',
                (data[0], data[1])):
            sqlite_connection.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Error while inserting data", error)
        return False
