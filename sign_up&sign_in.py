def staff_sign_up():
    #usr inputs details
    cursor.execute('USE SCHOOL')
    cpr = int(input('enter cpr: '))
    name = input('enter name: ').lower()
    dept = input('enter department: ').lower()

    password = input('create password: ')

    #to generate staffid
    query = 'SELECT max(STAFF_ID) FROM STAFF'
    cursor.execute(query)
    result = cursor.fetchone()
    if result is None:
        staff_id = 'T0'
    else:
        staff_id = 'T'+ str(result[0][1:] + 1)

    #to insert details into table STAFF
    cmd= "INSERT INTO STAFF VALUES({}, '{}', '{}', {}, '{}', '{}')".format(staff_id, name, dept, cpr, password)
    cursor.execute(cmd)
    db.commit()

def staff_sign_in():
    # to enter staff id and check if in database
    while True:
        staff_id = int(input('enter staff id: '))
        cmd = 'SELECT STAFFID FROM STAFF'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if tuple(staffID) in records:
            break
        else:
            print('staff id entered does not exist')
            print('1. try again')
            print('2. create a new account')
            opt = int(input('enter option: '))

            if opt == 1:
                continue
            if opt == 2:
                #entered id doesnt exist so create a new one
                staffSignUp()

    password = input('enter password: ')
    
    cmd = 'SELECT STAFFID, PASSWORD FROM STAFF'
    cursor.execute()
    records = cursor.fetchall()
    while True:
        for record in records:
            if record[0] == staff_id and record[1] == password:
                break 
            else: 
                print('wrong password')
                password = int(input('enter password: '))


    user_id = staff_id
    global user_id
    global user_type 
    user_type = 'staff'
    
    print('welcome to the database :)')

def student_sign_in():
    cursor.execute('USE STUDENT')
    
    while True:
        student_id = int(input('enter student id: '))
        cmd = 'SELECT STUDENT_ID FROM STUDENT'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if tuple(studentID) in records:
            break
        else:
            print('student id entered does not exist')
            print('try again')
            

    password = input('enter password: ')
    
    cmd = 'SELECT STUDENT_ID, PASSWORD FROM STUDENT'
    cursor.execute()
    records = cursor.fetchall()
    while True:
        for record in records:
            if record[0] == student_id and record[1] == passwd:
                break 
            else: 
                print('wrong password OR password doesnt match user')
                passwd = int(input('enter password: '))

    user_id = studentID

    global user_id
    global user_type 
    user_type = 'student'
    
    print('welcome to the database :)')











