# docstring- Lizzie Howe- airplane database application
# imports
import sqlite3

# constants and variables
DATABASE = "fighters.db"


# functions
def print_all_aircraft():
    '''print all the aircraft nicely'''
    db = sqlite3.connect("fighters.db")
    cursor = db.cursor()
    sql = "select * from fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''

name                          speed   max_g climb range payload
                            ''')
    for fighter in results:
        print(
            f"{fighter[1]:<30}"
            f"{fighter[2]:<8}"
            f"{fighter[3]:<6}"
            f"{fighter[4]:<6}"
            f"{fighter[5]:<6}"
            f"{fighter[6]:<6}"
            )
    # loop finished here
    db.close()


def print_all_aircraft_with_id():
    '''include aircraft id in printed table'''
    db = sqlite3.connect("fighters.db")
    cursor = db.cursor()
    sql = "select * from fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''

id      name                          speed   max_g climb range payload
                            ''')
    for fighter in results:
        print(
            f"{fighter[0]:<6}"
            f"{fighter[1]:<30}"
            f"{fighter[2]:<8}"
            f"{fighter[3]:<6}"
            f"{fighter[4]:<6}"
            f"{fighter[5]:<6}"
            f"{fighter[6]:<6}"
            )
    # loop finished here
    db.close()


def print_all_aircraft_by_speed():
    '''print all the aircraft sorted by speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from fighter ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''
name                          speed   max_g climb range payload
                            ''')
    for fighter in results:
        print(
            f"{fighter[1]:<30}"
            f"{fighter[2]:<8}"
            f"{fighter[3]:<6}"
            f"{fighter[4]:<6}"
            f"{fighter[5]:<6}"
            f"{fighter[6]:<6}"
            )
    # loop finished here
    db.close()


def print_all_aircraft_by_g():
    '''print all the aircraft sorted by max g'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from fighter ORDER BY max_g DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''
name                          speed   max_g climb range payload
                            ''')
    for fighter in results:
        print(
            f"{fighter[1]:<30}"
            f"{fighter[2]:<8}"
            f"{fighter[3]:<6}"
            f"{fighter[4]:<6}"
            f"{fighter[5]:<6}"
            f"{fighter[6]:<6}"
            )
    # loop finished here
    db.close()


def print_all_aircraft_by_climb():
    '''print all the aircraft sorted by climb speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from fighter ORDER BY climbrate DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''
name                          speed   max_g climb range payload
                            ''')
    for fighter in results:
        print(
            f"{fighter[1]:<30}"
            f"{fighter[2]:<8}"
            f"{fighter[3]:<6}"
            f"{fighter[4]:<6}"
            f"{fighter[5]:<6}"
            f"{fighter[6]:<6}"
            )
    # loop finished here
    db.close()


def print_all_aircraft_by_range():
    '''print all the aircraft sorted by range'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from fighter ORDER BY range DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''
name                          speed   max_g climb range payload
                            ''')
    for fighter in results:
        print(
            f"{fighter[1]:<30}"
            f"{fighter[2]:<8}"
            f"{fighter[3]:<6}"
            f"{fighter[4]:<6}"
            f"{fighter[5]:<6}"
            f"{fighter[6]:<6}"
            )
    # loop finished here
    db.close()


def print_all_aircraft_by_payload():
    '''print all the aircraft sorted by payload'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from fighter ORDER BY payload DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''
name                          speed   max_g climb range payload
                            ''')
    for fighter in results:
        print(
            f"{fighter[1]:<30}"
            f"{fighter[2]:<8}"
            f"{fighter[3]:<6}"
            f"{fighter[4]:<6}"
            f"{fighter[5]:<6}"
            f"{fighter[6]:<6}"
            )
    # loop finished here
    db.close()


def take_user_input():
    '''add a user intput into the database'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    aircraft TEXT,
                    speed INTEGER
                    max_g REAL
                    climbrate INTEGER
                    range INTEGER
                    payload INTEGER
                )''')

    aircraft = input("Enter the aircraft name: ")
    speed = int(input("Enter the speed: "))
    max_g = float(input("Enter the max_g: "))
    climbrate = int(input("Enter the climbrate: "))
    range = int(input("Enter the range: "))
    payload = int(input("Enter the payload: "))
    cursor.execute(
        '''INSERT INTO fighter (aircraft, speed, max_g, climbrate, range,
        payload) VALUES (?, ?, ?, ?, ?, ?)''',
        (aircraft, speed, max_g, climbrate, range, payload))

    db.commit()
    db.close()
    print('''
            Aircraft accepted''')


def remove_user_input():
    '''remove an intput from the database'''
    while True:
        # show user the current data (with id)
        print_all_aircraft_with_id()
        id = int(input("""
Which aircraft would you like to delete? Type 0 to cancel.
"""))
        if id == 0:
            break
        else:
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = "DELETE FROM fighter WHERE id = ?;"
            cursor.execute(sql, (id,))
            db.commit()
            print("""
                Aircraft""", id, """successfully deleted""")


# main code
while True:
    user_input = input(
        """

    What would you like to do?
    1. Print all aircraft
    2. Print all aircraft sorted by speed
    3. Print all aircraft sorted by max g force
    4. Print all aircraft sorted by climb
    5. Print all aircraft sorted by range
    6. Print all aircraft sorted by payload
    7. Add an input
    8. Remove an input
    9. Exit
""")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_by_speed()
    elif user_input == "3":
        print_all_aircraft_by_g()
    elif user_input == "4":
        print_all_aircraft_by_climb()
    elif user_input == "5":
        print_all_aircraft_by_range()
    elif user_input == "6":
        print_all_aircraft_by_payload()
    elif user_input == "7":
        take_user_input()
    elif user_input == "8":
        remove_user_input()
    elif user_input == "9":
        break
    else:
        print("That is not an option\n")
