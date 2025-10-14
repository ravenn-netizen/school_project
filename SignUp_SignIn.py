def staffSignUp():
    #usr inputs details
    cursor.execute('USE STUDENT')
    cpr = int(input('enter cpr: '))
    name = input('enter name: ').capitalize()
    dept = input('enter department: ').lower()

    passwd1 = input('create password: ')

    #to generate staffid
    query = 'SELECT max(STAFF_ID) FROM STAFF'
    cursor.execute(query)
    staffid = cursor.fetchone() + 1

    #to insert details into table STAFF
    cmd= "INSERT INTO STAFF VALUES({}, '{}', '{}', {}, '{}', '{}')".format(staffid, name, dept, cpr, passwd1)
    cursor.execute(cmd)

def StaffSignIn():
    # to enter staff id and check if in database
    while True:
        staffid = int(input('enter staffid: '))
        cmd = 'SELECT STAFFID FROM STAFF'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if tuple(staffid) in records:
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
    
    cmd = 'SELECT STAFFID, PASSWD FROM STAFF'
    cursor.execute()
    records = cursor.fetchall()
    while True:
        for record in records:
            if record[0] == staffid and record[1] == passwd:
                break 
            else: 
                print('wrong password')
                passwd = int(input('enter passwd: '))

    print('welcome into the database :)')

def studentSignIn():
    cursor.execute('USE STUDENT')
    
    while True:
        studentId = int(input('enter student id: '))
        cmd = 'SELECT STUDID FROM STUDENT'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if tuple(studentId) in records:
            break
        else:
            print('student id entered does not exist')
            print('try again')
            

    passwd = input('enter password: ')
    
    cmd = 'SELECT STUDENTID, PASSWORD FROM STAFF'
    cursor.execute()
    records = cursor.fetchall()
    while True:
        for record in records:
            if record[0] == studentId and record[1] == passwd:
                break 
            else: 
                print('wrong password')
                passwd = int(input('enter passwd: '))
                
    print('welcome into the database :)')


