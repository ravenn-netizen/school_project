#complete
#under testing

def staff_sign_in():
    # to enter staff id and check if in database
    cursor.execute('USE SCHOOL')
    
    while True:
        staff_id =int(input('enter staff id: '))
        cmd = 'SELECT STAFF_ID FROM STAFF'
        cursor.execute(cmd)
        records = cursor.fetchall()

        if (staff_id,) in records:
            break
        else:
            print(records)
            print('staff id entered does not exist')
            print('1. try again')
            print('2. exit to main menu')
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
            return staff_id
        else: 
            print('wrong password')
            print('1. try password again')
            print('2. exit to main menu')
            opt = int(input('enter option: '))
            if opt == 1:
                continue
            if opt == 2:
                return 0
    
    print('welcome to the database :)')
#also include the below three lines of code when using the function          
user_id = staff_sign_in()
if user_id == 0:
    continue

def student_sign_in():
    cursor.execute('USE SCHOOL')
    
    while True:
        student_id = int(input('enter student id: '))
        cmd = 'SELECT STUDENT_ID FROM STUDENT'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if (student_id,) in records:
            break
        else:
            print('student id entered does not exist')
            print('1. try again')
            print('2. exit to main menu')
            opt = int(input('enter option: '))

            if opt == 1:
                continue
            elif opt == 2:
                return 0
    
    cmd = "SELECT PASSWORD FROM STUDENT WHERE STUDENT_ID = '{}'".format(student_id)
    cursor.execute(cmd)
    password_in_db = cursor.fetchall()[0]

    while True: 
        entered_password = input('enter password: ')
        if entered_password == password_in_db:
            return student_id
        else: 
            print('wrong password')
            print('1. try password again')
            print('2. exit to main menu')
            opt = int(input('enter option: '))
            if opt == 1:
                continue
            if opt == 2:
                return 0

    print('welcome to the database :)')  
    
#also include the below three lines of code when using the function          
user_id = student_sign_in()
if user_id == 0:
    continue
    
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
                      
def admin_menu():
    print("--- MENU ---")
    print("1. staff management")
    print("2. student management")

    opt = int(input("enter option: "))

    if opt == 1:
        new_staff()

    if opt == 2:
        print("1. new student")
        print("2. search student")
        print("3. remove student")
        choice = int(input("Enter choice :"))
        if choice == 1:
            new_student()
        elif choice == 2:
            searchSTUDENTID()
        elif choice == 3:
            delstudent()






