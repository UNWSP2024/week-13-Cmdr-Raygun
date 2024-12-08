# Author: Andrew Bittner
# Date: 12/7/2024
# Program #4: Phonebook Database Manipulation

import sqlite3

class DBManipulator:
    def __init__(self):

        # Set flags.
        self.loop_run = False

        # Connect to database.
        self.conn = sqlite3.connect("phonebook.db")
        self.cur = self.conn.cursor()

        # Start main input loop.
        while True:

            # Check to see if loop has already run; if not, display list of commands.
            if not self.loop_run:
                print('Choose operation from following:\n\n    "read" to read the contents of the entire table\n'
                      '    "add" to add a new row\n    "edit" to edit a row\n    "delete" to delete a row\n    "exit" '
                      'to exit program\n    "help" for a list of commands')
                self.loop_run = True

            # Get input and perform the corresponding command.
            self.choice = input('\n> ')
            if self.choice.lower() == 'read':
                self.read_table()
            elif self.choice.lower() == 'add':
                self.add_row()
            elif self.choice.lower() == 'edit':
                self.edit_row()
            elif self.choice.lower() == 'delete':
                self.delete_row()
            elif self.choice.lower() == 'help':
                self.show_help()
            elif self.choice.lower() == 'exit':
                break
            else:
                print('Please select a valid operation.')

        # Close database connection.
        self.conn.close()

        # End program.
        exit_sequence()

    def read_table(self):

        # Read and print rows from the Contacts table.
        for row in self.cur.execute('''SELECT * FROM Contacts'''):
            print(f'ID: {row[0]}; Name: {row[1]}; Phone #: {row[2]}')

    def add_row(self):
        while True:

            # Get name and number for new row in Contacts table.
            inp = input('Enter the name for the new contact; alternatively, enter '
                         '"exit" to cancel: ')
            if inp.lower() == 'exit':
                break
            name = inp
            inp = input('Enter the phone number: ')
            if inp.lower() == 'exit':
                break
            num = inp

            # Add row to Contacts table.
            self.cur.execute('''INSERT INTO Contacts (ContactName, PhoneNum) VALUES (?, ?)''', (name,
                             num))
            print('Contact added successfully.')
            break

        # Commit changes.
        self.conn.commit()

    def edit_row(self):

        # Create a list holding contents of Contacts table (used for input validation).
        contacts_list = []
        for row in self.cur.execute('''SELECT * FROM Contacts'''):
            contacts_list.append(row)

        # Input loop for getting contact ID.
        while True:
            inp = input('Enter the ID of the contact you would like to modify; alternatively, enter "exit" to cancel: ')
            if inp.lower() == 'exit':
                break

            # Verify that input both is an integer and is the ID (primary key) of an existing contact.
            try:
                for row in contacts_list:
                    if int(inp) == row[0]:
                        id_sel = int(inp)
                        break
                inp = str(id_sel)
            except (ValueError, UnboundLocalError):
                print('Please select a valid ID.')
            else:
                break

        # Input loop for getting attribute to be modified. Once valid ID has been taken from user, program asks if the
        # user would like to change the name, phone number, or both.
        while not inp.lower() == 'exit':
            # self.entry_old = self.cur.execute('''SELECT * FROM Contacts WHERE ContactID=:v''', {"v": 1})
            inp = input('Enter the attribute of the contact you would like to edit ("name",'
                        ' "number", or "all"); alternatively, enter "exit" to cancel: ')
            if inp.lower() == 'exit':
                break

            # Change name, if requested by user.
            if inp.lower() == 'name':
                inp = input('Enter the new name: ')
                if inp.lower() == 'exit':
                    break
                attr_new = inp
                self.cur.execute('''UPDATE Contacts SET ContactName = ? WHERE ContactID == ?''', (attr_new,
                                 id_sel))
                print('Contact name updated successfully.')
                break

            # Change phone number, if requested by user.
            elif inp.lower() == 'number':
                inp = input('Enter the new phone number: ')
                if inp.lower() == 'exit':
                    break
                attr_new = inp
                self.cur.execute('''UPDATE Contacts SET PhoneNum = ? WHERE ContactID == ?''',
                                 (attr_new, id_sel))
                print('Contact phone number updated successfully.')
                break

            # Change name and phone number, if requested by user.
            elif inp.lower() == 'all':
                inp = input('Enter the new name: ')
                if inp.lower() == 'exit':
                    break
                attr_new = inp
                self.cur.execute('''UPDATE Contacts SET ContactName = ? WHERE ContactID == ?''', (attr_new,
                                 id_sel))
                inp = input('Enter the new phone number: ')
                if inp.lower() == 'exit':
                    break
                attr_new = inp
                self.cur.execute('''UPDATE Contacts SET PhoneNum = ? WHERE ContactID == ?''',
                                 (attr_new, id_sel))
                print('Contact name and phone number updated successfully.')
                break
            else:
                print('Please select a valid operation.')

        # Commit changes.
        self.conn.commit()

    def delete_row(self):

        # Create a list holding contents of Contacts table (used for input validation).
        contacts_list = []
        for row in self.cur.execute('''SELECT * FROM Contacts'''):
            contacts_list.append(row)

        # Input loop for getting contact ID.
        while True:
            inp = input('Enter the ID of the phonebook contact you would like to delete; alternatively, enter '
                             '"exit" to cancel: ')

            # Verify that input both is an integer and is the ID (primary key) of an existing contact.
            try:
                for row in contacts_list:
                    if int(inp) == row[0]:
                        id_sel = int(inp)
                        break
                inp = str(id_sel)
            except (ValueError, UnboundLocalError):
                print('Please select a valid ID.')
            else:
                break

        # Delete contact.
        self.cur.execute('''DELETE FROM Contacts WHERE ContactID == ?''', inp)
        print('Contact deleted successfully.')

        # Commit changes.
        self.conn.commit()

    def show_help(self):
        print('Possible commands:\n\n    "read" to read the contents of the entire table\n    "add" to add a new '
              'row\n    "edit" to edit a row\n    "delete" to delete a row\n    "exit" to exit program\n    "help" '
              'for a list of commands')

def exit_sequence():
        # Function to keep console/window open until user ends program.
        input('\n\nPress [enter] to exit... ')

if __name__ == '__main__':
    db_man_1 = DBManipulator()