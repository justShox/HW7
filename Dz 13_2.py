import sqlite3

sql = sqlite3.connect('mydatabase.db')

connect = sql.cursor()

connect.execute("CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMERY KEY, name TEXT, age INTEGER, grade TEXT);")

connect.execute('INSERT INTO Students (name, age, grade) VALUES ("Martin", 20, "A");')
connect.execute('INSERT INTO Students (name, age, grade) VALUES ("Jacob", 21, "B");')
connect.execute('INSERT INTO Students (name, age, grade) VALUES ("Jenny", 19, "C");')
connect.execute('INSERT INTO Students (name, age, grade) VALUES ("Alex", 20, "F");')
connect.execute('INSERT INTO Students (name, age, grade) VALUES ("Katy", 24, "A");')


def get_student_by_name():

    """Printing all the info about the students"""
    name = str(input("Enter the name: ")).strip().title()
    connect.execute("SELECT name FROM Students WHERE name = ?", (name,))
    check_name = connect.fetchone()
    if check_name:
        print(connect.execute("SELECT * FROM Students WHERE name=?;", (name,)).fetchone())
    else:
        print("No such student!")


def update_student_grade():

    """Updating the student's grade"""
    name = str(input("Enter the name: ")).strip().title()
    new_grade = str(input("Enter new grade: ")).strip().title()
    connect.execute("SELECT name FROM Students WHERE name = ?", (name,))
    check_name = connect.fetchone()
    if check_name:
        if new_grade == "A" or new_grade == "B" or new_grade == "C" or new_grade == "D" or new_grade == "F":
            print('Grade has been updated 📝!')
            print(connect.execute("UPDATE Students SET grade=? WHERE name=?;", (new_grade, name)).fetchone())
        else:
            print('No such grade!')
    else:
        print("No such student!")


def delete_student():

    """Deletion of the student from the database"""
    name = str(input("Enter the name: ")).strip().title()
    connect.execute("SELECT name FROM Students WHERE name = ?", (name,))
    check_name = connect.fetchone()
    if check_name:
        print(f'Student {name} has been deleted 🗑')
        print(connect.execute("DELETE FROM Students WHERE name=?;", (name,)).fetchone())
    else:
        print("No such student!")


def info_all():
    print(connect.execute("SELECT * FROM Students;").fetchall())


while True:
    command = str(input('Enter your command: ')).lower().strip()
    if command == 'info':
        get_student_by_name()
    elif command == 'update':
        update_student_grade()
    elif command == 'delete':
        delete_student()
    elif command == 'info all':
        info_all()
    else:
        print('No such command 🚫')
