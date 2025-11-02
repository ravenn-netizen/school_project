def staff_sign_up():
    #usr inputs details
    cursor.execute('USE SCHOOL')
    cpr = int(input('enter cpr: '))
    name = input('enter name: ').lower()
    dept = input('enter department: ').lower()

    #here admin is creating acc for staff; so password is set default to 'password' until changed by the staff themselves
    password = "password"

    #to generate staffid
    # staffid eg T0, T1, T2, T78 (basically 'T' + a number)
    query = 'SELECT max(STAFF_ID) FROM STAFF'
    cursor.execute(query)
    result = cursor.fetchone()
    if result[0] is None: #this is in case the table is empty and there are no values for staffid, in that case im creating a new one ie 'T0'
        staff_id = 'T0'
    else:
        #this is in case there are already some records inthe table
        # result[0] to access the id, cuz sql returns it in a tuple
        # result[0][1:] using slicing t extraxt the numerical part; then converting it into int(), then adding +1
        # for new id convert into string, concatenate to T, AND VOILA! NEW STAFF ID GUYSS!!
        #this code is cryptic aff ikk so lmk if can find something simpler
        staff_id = 'T'+ str(int(result[0][1:]) + 1)

    #to insert details into table STAFF
    cmd= "INSERT INTO STAFF VALUES('{}', '{}', '{}','{}', '{}')".format(staff_id, name, dept, cpr, password)
    cursor.execute(cmd)
    db.commit()

def staff_sign_in():
    # to enter staff id and check if in database
    while True:
        staff_id =input('enter staff id: ')
        cmd = 'SELECT STAFF_ID FROM STAFF'
        cursor.execute(cmd)
        records = cursor.fetchall()

        if (staff_id,) in records:
            print(records)
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
    password_in_db = cursor.fetchall()[0]

    while True:
        entered_password = input('enter password: ')
        if entered_password == password_in_db:
            return 1 
        else: 
            print('wrong password')
            print('1. try password again')
            print('2. exit to main menu')
            opt = int(input('enter option: '))
            if opt == 1:
                continue
            if opt == 2:
                return 0

    
    global user_id
    user_id = staff_id
    global user_type 
    user_type = 'staff'
    
    print('welcome to the database :)')

def student_sign_in():
    cursor.execute('USE SCHOOL')
    
    while True:
        student_id = input('enter student id: ')
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
            

    
    cmd = "SELECT PASSWORD FROM STAFF WHERE STAFF_ID = '{}'".format(staff_id)
    cursor.execute(cmd)
    password_in_db = cursor.fetchall()[0]

    while True: 
        entered_password = input('enter password: ')
        if entered_password == password_in_db:
            return 1 
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

    global user_id
    user_id = student_id
    global user_type 
    user_type = 'student'
    
    print('welcome to the database :)')

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
        print("1. add new staff")
        print("2. search staff")
        print("3. remove staff")

    if opt == 2:
        print("1. new student")
        print("2. search student")
        print("3. remove student")

