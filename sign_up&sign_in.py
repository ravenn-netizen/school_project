def staff_sign_up():
    #usr inputs details
    cursor.execute('USE SCHOOL')
    cpr = int(input('enter cpr: '))
    name = input('enter name: ').lower()
    dept = input('enter department: ').lower()

    password = input('create password: ')

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
            print('2. create a new account')
            opt = int(input('enter option: '))

            if opt == 1:
                continue
            if opt == 2:
                #entered id doesnt exist so create a new one
                staffSignUp()

    password = input('enter password: ')
    
    cmd = 'SELECT STAFF_ID, PASSWORD FROM STAFF'
    cursor.execute(cmd)
    records = cursor.fetchall()
    while True:
        for record in records:
            if record[0] == staff_id and record[1] == password:
                break 
        else: 
            print('wrong password')
            password = input('enter password: ')
    print('welcome to the database :)')


    
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
            print('try again')
            

    password = input('enter password: ')
    
    cmd = 'SELECT STUDENT_ID, PASSWORD FROM STUDENT'
    cursor.execute(cmd)
    records = cursor.fetchall()
    while True:
        for record in records:
            if record[0] == student_id and record[1] == password:
                break 
        else: 
                print('wrong password OR password doesnt match user')
                password =input('enter password: ')

    print('welcome to the database :)')   

    global user_id
    user_id = student_id
    global user_type 
    user_type = 'student'
    
    print('welcome to the database :)')
