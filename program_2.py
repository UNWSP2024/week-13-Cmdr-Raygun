# Author: Andrew Bittner
# Date: 12/6/2024
# Program #2: Cities Database Display

import sqlite3

def main():
    # Connect to database.
    conn = sqlite3.connect("cities.db")
    cur = conn.cursor()

    # Read and print rows from the Cities table.
    for row in cur.execute('''SELECT * FROM Cities'''):
        print(f'City: {row[1]}; Pop.: {round(row[2])}')

    # Close database connection.
    conn.close()

    # End program.
    print('\nEnd of data in Cities table.')
    exit_sequence()

def exit_sequence():
    # Function to keep console/window open until user ends program.
    input('\n\nPress [enter] to exit... ')

if __name__ == '__main__':
    main()