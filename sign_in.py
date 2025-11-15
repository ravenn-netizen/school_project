def staff_sign_in():
    # to enter staff id and check if in database
    
    while True:
        staff_id =int(input('enter staff id: '))
        cmd = 'SELECT STAFF_ID FROM STAFF'
        cursor.execute(cmd)
        records = cursor.fetchall()

        if (staff_id,) in records:
            break
        else:
            print(records)
            print('\nstaff id entered does not exist')
            print('1. try again')
            print('2. exit to main menu\n')
            opt = int(input('enter option: '))

            if opt == 1:
                continue
            elif opt == 2:
                return 0     

    cmd = "SELECT PASSWORD FROM STAFF WHERE STAFF_ID = '{}'".format(staff_id)
    cursor.execute(cmd)
    password_in_db = cursor.fetchone()[0]

    while True:
        entered_password = input('enter password: ')
        if entered_password == password_in_db:
            print("Hello, staff '{}'".format(staff_id))
            print("Welcome to the database.\n")
            return staff_id
        else: 
            print('\nwrong password')
            print('1. try password again')
            print('2. exit to main menu\n')
            opt = int(input('enter option: '))
            if opt == 1:
                continue
            if opt == 2:
                return 0
    
def student_sign_in():
    
    while True:
        student_id = int(input('enter student id: '))
        cmd = 'SELECT STUDENT_ID FROM STUDENT'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if (student_id,) in records:
            break
        else:
            print('\nstudent id entered does not exist')
            print('1. try again')
            print('2. exit to main menu\n')
            opt = int(input('enter option: '))

            if opt == 1:
                continue
            elif opt == 2:
                return 0
    
    cmd = "SELECT PASSWORD FROM STUDENT WHERE STUDENT_ID = '{}'".format(student_id)
    cursor.execute(cmd)
    password_in_db = cursor.fetchone()[0]

    while True: 
        entered_password = input('enter password: ')
        if entered_password == password_in_db:
            print('Hello, student "{}"!'.format(student_id))
            print('Welcome to the database.\n')
            return student_id
        else: 
            print('\nwrong password')
            print('1. try password again')
            print('2. exit to main menu\n')
            opt = int(input('enter option: '))
            if opt == 1:
                continue
            if opt == 2:
                return 0

def admin_sign_in():
    set_password = "admin's password"

    while True:
        entered_password = input('Enter password: ')
        if entered_password == set_password:
            return 1
        else:
            print('wrong password')
            print("1. try password again")
            print("2. exit to main menu")
            opt = int(input("enter option: "))
            if opt == 1:
                continue
            else:
                return 0 #user is not signed in and gets returned to main menu #refer menu() for reference
