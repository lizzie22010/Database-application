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
    print("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
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
    print ("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
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
    print ("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
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
    print ("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
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
    print ("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()


def print_all_aircraft_by_payload():
    '''print all the aircraft sorted by payload'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from fighter ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print ("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()


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
7. Exit
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
        break
    else:
        print("That was not an option\n")
