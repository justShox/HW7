import sqlite3

connection = sqlite3.connect('Bank account.db')

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clients (surname TEXT, name TEXT, last_name TEXT, phone_number INTEGER,"
               "balance REAL);")

"""Taking input from user:"""


def registration():
    surname = str(input("Enter your surname 🔠: ")).title().strip()
    name = str(input("Enter your name 🔠: ")).title().strip()
    last_name = str(input("Enter your last name 🔠: ")).title().strip()
    phone_number = input("Enter your phone number (with +) 📲: ").strip()
    balance = float(input("Enter the money you have ($) 💰: "))

    """Checking entered info"""
    if len(surname) > 12 or len(surname) < 3:
        print('Invalid input surname length')
    elif len(name) > 12 or len(name) < 3:
        print('Invalid input name length')
    elif len(last_name) > 12 or len(last_name) < 3:
        print('Invalid input last name length')
    elif len(phone_number) > 14 or len(phone_number) < 12:
        print('Invalid phone number.')
    elif balance < 0 or balance > 10 ** 10:
        print('Invalid balance')
    else:

        """Inserting the info"""
        cursor.execute("INSERT INTO clients (surname, name, last_name, phone_number, balance) VALUES (?,?,?,?,?)",
                       (surname, name, last_name, phone_number, balance))

        connection.commit()
        print('Client was added successfully ✅')
        print(cursor.execute("SELECT * FROM clients;").fetchall())


def find_the_client_name():

    """Find client by name"""
    name = str(input("Enter your name: ")).title().strip()
    cursor.execute("SELECT name FROM clients WHERE name = ?", (name,))
    check_name = cursor.fetchone()
    if check_name:
        print('Here is the info about the client 👇')
        print(cursor.execute("SELECT * FROM clients WHERE name = ?;", (name,)).fetchall())
    else:
        print('No such client⚠️! Register first!')


def find_the_client_surname():

    """Find client by surname"""
    surname = str(input("Enter your surname: ")).title().strip()
    cursor.execute("SELECT surname FROM clients WHERE surname = ?", (surname,))
    check_surname = cursor.fetchone()
    if check_surname:
        print('Here is the info about the client 👇')
        print(cursor.execute("SELECT * FROM clients WHERE surname = ?;", (surname,)).fetchall())
    else:
        print('No such client⚠️! Register first!')


def find_the_client_last_name():

    """Find client by surname"""
    last_name = str(input("Enter your last name: ")).title().strip()
    cursor.execute("SELECT last_name FROM clients WHERE last_name = ?", (last_name,))
    check_surname = cursor.fetchone()
    if check_surname:
        print('Here is the info about the client 👇')
        print(cursor.execute("SELECT * FROM clients WHERE last_name = ?;", (last_name,)).fetchall())
    else:
        print('No such client⚠️! Register first!')


def find_the_client_phone_number():

    """Finding client by phone number"""
    phone_number = str(input("Enter your phone number(with +) 📲: "))
    check_phone_number = cursor.execute("SELECT phone_number FROM clients WHERE phone_number =?",
                                        (phone_number,)).fetchone()
    if check_phone_number:
        print('Here is the info about the client ⬇️')
        print(cursor.execute("SELECT * FROM clients WHERE phone_number = ?", (phone_number,)).fetchall())
    else:
        print('No such client⚠️! Register first!')


def add_to_balance():

    """Adding money to balance"""
    name = str(input("Enter your name 🔍: ")).title().strip()
    add = float(input('Enter amount of money you want to add 💰: '))
    cursor.execute("SELECT name FROM clients WHERE name = ?", (name,))
    check_name = cursor.fetchone()
    if check_name:
        connection.commit()
        print('Balance changed successfully')
        print(cursor.execute("UPDATE clients SET balance = balance + ? WHERE name = ?",
                             (add, name)).fetchall())
    elif add < 0:
        print('Invalid amount')
    elif add > 10 ** 10:
        print('Too much money')
    else:
        print('No such client⚠️! Register first!')


def cash():

    """Cashing money from balance"""
    name = str(input("Enter your name: ")).title().strip()
    cash = float(input("Enter the amount of money you want to cash out: "))
    cursor.execute("SELECT balance FROM clients WHERE name = ?", (name,))
    balance = cursor.fetchone()[0]
    if cash < 0:
        print('Invalid cash amount ⚠️')
    elif balance < cash:
        print('Not enough money on the balance ⚠️!')
    else:
        connection.commit()
        print('Operation successful ✅')
        print(cursor.execute("UPDATE clients SET balance = balance - ? WHERE name = ?;",
                             (cash, name)).fetchone())


def view_balance():

    """Checking client balance"""
    name = str(input("Enter your name: ")).title().strip()
    check_name = cursor.execute('SELECT name FROM clients WHERE name = ?', (name,)).fetchone()
    if check_name:
        print('Your balance ⬇️:')
        print(cursor.execute("SELECT balance FROM clients WHERE name = ?", (name,)).fetchone())
    else:
        print('No such client⚠️! Register first!')


def investment():

    """Investing"""
    name = str(input("Enter your name 🔍: ")).title().strip()
    check_balance = cursor.execute("SELECT balance FROM clients WHERE name = ?", (name,)).fetchone()
    check_name = cursor.execute('SELECT name FROM clients WHERE name = ?', (name,)).fetchone()
    if check_name:
        if check_balance is not None:
            balance = check_balance[0]
            print('With your balance and investment rate 15%: ')
            print(f'For 12 month total sum is - ${balance * (1 + 0.15) * 1}')
            print(f'For 24 month total sum is - ${balance * (1 + 0.15) * 2}')
            print(f'For 36 month total sum is - ${balance * (1 + 0.15) * 3}')
    else:
        print('No such client⚠️! Register first!')


def view_client_profile():

    """View profile"""
    name = str(input("Enter your name to enter your profile 🔍: ")).title().strip()
    cursor.execute("SELECT name FROM clients WHERE name = ?", (name,))
    check_name = cursor.fetchone()
    if check_name:
        print('You are in your cabin ⬇️:')
        print(cursor.execute("SELECT * FROM clients WHERE name = ?",
                             (name,)).fetchall())
    else:
        print('No such client⚠️! Register first!')


def info_about_all_clients():

    """View all clients"""
    print(cursor.execute("SELECT * FROM clients;").fetchall())


while True:
    command = str(input("Enter your command 💬: ")).lower().strip()
    if command == 'register':
        registration()
    elif command == 'find name':
        find_the_client_name()
    elif command == 'find surname':
        find_the_client_surname()
    elif command == 'find last name':
        find_the_client_last_name()
    elif command == 'find phone number':
        find_the_client_phone_number()
    elif command == 'add balance':
        add_to_balance()
    elif command == 'cash':
        cash()
    elif command == 'balance':
        view_balance()
    elif command == 'investment':
        investment()
    elif command == 'profile':
        view_client_profile()
    elif command == 'info':
        info_about_all_clients()
    else:
        print('Invalid command!')
