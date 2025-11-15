streams={'H01':('English','Home Science','Psychology','Marketing','Sociology'), 'C01':('English','Accountancy','Business Studies','Economics','Mathematics'),'C02':('English','Accountancy','Business Studies','Economics','Informatics Practices'),'C03':('English','Accountancy','Business Studies','Economics','Marketing'),'S01':( 'English','Physics','Chemistry','Mathematics','Biology'),'S02':('English','Physics','Chemistry','Mathematics','Computer Science'),'S03':('English','Physics','Chemistry','Mathematics','Engineering Graphics'),'S04':('English','Physics','Chemistry','Biology','Computer Science'),'S05':('English','Physics','Chemistry','Biology','Bio-Technology'),'S06':('English','Physics','Chemistry','Mathematics','Artificial Intelligence')}

def new_student():

    name = input("enter name: ").title()
    dob = input('enter date of birth YYYY-MM-DD: ')
    gender = input('enter gender (M or F): ').upper().strip()

    age = int(input('Enter age: '))
    grade = int(input("enter class (11-12): "))
    section = input("enter section (A-Z): ").upper()
    
    # see guys i made a global dictionary that contain streamcode (eg: H01, C02, S03) and corresponding subjects
    # now im print the streamcode and its subjects to let the staff confirm that their entering the right stream code
    
    for stream_code, subjects in streams.items():
        print(stream_code, subjects)
  
    stream = input("enter streamcode: ").upper().strip()
    transport = input("enter transport (bus or private): ").lower().strip()

    if transport == 'bus':
        bus_no  = int(input("enter bus number: "))
        bus_stop = input("enter bus stop: ").lower()
    else:
        bus_no , bus_stop  = 0, 'None' 

    guardian = input("enter name of guardian(s) (each separated by a \' & \'): ").title()
    tel = input('enter phone number: ')
    email = input('enter email: ').strip()
    address = input('enter address ( [flat] & [building] & [road] & [block] & [area] ')
    cpr = input('enter student\'s cpr number: ').strip()

    #to generate new student_id
    cmd = "SELECT MAX(STUDENT_ID) FROM STUDENT"
    cursor.execute(cmd)
    result = cursor.fetchone()
    
    if result[0] is None or result==[]:
        student_id = 1
    else:
        student_id = result + 1
#password is set default to password until changed by the student
    password = 'password'
    print('Generated student id is', student_id)
    
    cmd = "INSERT INTO STUDENT VALUES({}, '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}' ,'{}')".format(student_id, name, dob, gender, age, grade, section, stream, transport, bus_no, bus_stop, guardian, tel, email, address,cpr, password)
    cursor.execute(cmd)
    db.commit()


def new_staff():
    #usr inputs details
    cpr = int(input('enter cpr: '))
    name = input('enter name: ').lower()
    dept = input('enter department: ').lower()

    #here admin is creating acc for staff; so password is set default to 'password' until changed by the staff themselves
    password = "password"

    #to generate staffid
    query = 'SELECT max(STAFF_ID) FROM STAFF'
    cursor.execute(query)
    result = cursor.fetchone()
    if not result:
        staff_id = 1
    else:
        staff_id = result[0] + 1
    print('Generated staff id is', staff_id)

    #to insert details into table STAFF
    cmd= "INSERT INTO STAFF VALUES({}, '{}', '{}','{}', '{}')".format(staff_id, name, dept, cpr, password)
    cursor.execute(cmd)
    db.commit()

