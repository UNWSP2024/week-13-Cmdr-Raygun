# Author: Andrew Bittner
# Date: 12/6/2024
# Program #1: Cities Database Setup

import sqlite3

def main():
    try:
        # Try opening the database as a text file; if it doesn't exist (if an IOError is thrown), database will be
        # created and populated
        cities_txt = open("cities.db", "r")
        cities_txt.close()
        print('Database already exists.')
        exit_sequence()

    except IOError:
        # Create list of cities, complete with attributes.
        list_cities = [('Minneapolis', 425115), ('Saint Paul', 303820), ('Rochester', 122413), ('Duluth', 87680),
                       ('Bloomington', 87398), ('Brooklyn Park', 82017), ('Woodbury', 79538), ('Plymouth', 77648),
                       ('Lakeville', 76243), ('Blaine', 73774), ('Maple Grove', 71288), ('St. Cloud', 71013),
                       ('Eagan',67396), ('Burnsville', 64772), ('Coon Rapids', 63377), ('Eden Prairie', 62166),
                       ('Apple Valley', 55336), ('Edina', 53348), ('Minnetonka', 52463), ('St. Louis Park', 49697)]

        # Create and connect to database.
        conn = sqlite3.connect("cities.db")
        cur = conn.cursor()

        # Create table.
        cur.execute('''CREATE TABLE IF NOT EXISTS Cities (CityID INTEGER PRIMARY KEY, CityName TEXT, Population REAL)''')

        # Populate database.
        cur.executemany('''INSERT INTO Cities (CityName, Population) VALUES (?, ?)''', list_cities)

        # Commit changes.
        conn.commit()

        # Close database connection.
        conn.close()

        # End program.
        print('Database created successfully.')
        exit_sequence()

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

if __name__ == '__main__':
    main()