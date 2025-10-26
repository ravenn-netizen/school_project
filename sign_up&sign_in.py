def staff_sign_up():
    #usr inputs details
    cursor.execute('USE SCHOOL')
    cpr = int(input('enter cpr: '))
    name = input('enter name: ').lower()
    dept = input('enter department: ').lower()

    passwd1 = input('create password: ')

    #to generate staffid
    query = 'SELECT max(STAFF_ID) FROM STAFF'
    cursor.execute(query)
    staffid = cursor.fetchone() + 1

    #to insert details into table STAFF
    cmd= "INSERT INTO STAFF VALUES({}, '{}', '{}', {}, '{}', '{}')".format(staffid, name, dept, cpr, passwd1)
    cursor.execute(cmd)
    db.commit()

def staff_sign_in():
    # to enter staff id and check if in database
    while True:
        staffID = int(input('enter staffid: '))
        cmd = 'SELECT STAFFID FROM STAFF'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if tuple(staffID) in records:
            break
        else:
            print('staffid entered does not exist')
            print('1. try again')
            print('2. create a new account')
            opt = int(input('enter option: '))

            if opt == 1:
                continue
            if opt == 2:
                #entered id doesnt exist so create a new one
                staffSignUp()

    passwd = input('enter password: ')
    
    cmd = 'SELECT STAFFID, PASSWORD FROM STAFF'
    cursor.execute()
    records = cursor.fetchall()
    while True:
        for record in records:
            if record[0] == staffID and record[1] == passwd:
                break 
            else: 
                print('wrong password')
                passwd = int(input('enter passwd: '))
                
    query = "SELECT CPR FROM STAFF WHERE STUDENTID = {}".format(staffID)    
    cursor.execute(query)
    cpr  = cursor.fetchone()

    user_id = staffID

    #this cpr and staffID will be used to reference the user gliabally 
    global cpr
    global user_id
    global user_type 
    user_type = 'staff'
    
    print('welcome to the database :)')

def student_in():
    cursor.execute('USE STUDENT')
    
    while True:
        studentID = int(input('enter student id: '))
        cmd = 'SELECT STUDENTID FROM STUDENT'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if tuple(studentID) in records:
            break
        else:
            print('student id entered does not exist')
            print('try again')
            

    passwd = input('enter password: ')
    
    cmd = 'SELECT STUDENTID, PASSWORD FROM STUDENT'
    cursor.execute()
    records = cursor.fetchall()
    while True:
        for record in records:
            if record[0] == studentID and record[1] == passwd:
                break 
            else: 
                print('wrong password')
                passwd = int(input('enter password: '))

    query = "SELECT CPR FROM STUDENT WHERE STUDENTID = {}".format(studentID)    
    cursor.execute(query)

    #this cpr and student ID will be used to reference the user globally
    cpr  = cursor.fetchone()
    user_id = studentID

    global cpr
    global user_id
    global user_type 
    user_type = 'student'
    
    print('welcome to the database :)')









