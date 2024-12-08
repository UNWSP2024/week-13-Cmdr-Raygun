# Author: Andrew Bittner
# Date: 12/6/2024
# Program #1: Phonebook Database Setup

import sqlite3

def main():
    try:
        # Try opening the database as a text file; if it doesn't exist (if an IOError is thrown), database will be
        # created and populated
        phonebook_txt = open("phonebook.db", "r")
        phonebook_txt.close()
        print('Database already exists.')
        exit_sequence()

    except IOError:
        # Create list of cities, complete with attributes.
        list_phonebook = [('Jenny', '867-5309')]

        # Create and connect to database.
        conn = sqlite3.connect("phonebook.db")
        cur = conn.cursor()

        # Create table.
        cur.execute('''CREATE TABLE IF NOT EXISTS Contacts (ContactID INTEGER PRIMARY KEY, ContactName TEXT, PhoneNum TEXT)''')

        # Populate database.
        cur.executemany('''INSERT INTO Contacts (ContactName, PhoneNum) VALUES (?, ?)''', list_phonebook)

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