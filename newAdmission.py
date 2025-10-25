def newAdmission():
    name = input("enter name: ")
    dob = input('enter date of birth YYYY-MM-DD: ')
    gender = input('enter gender (M or F): ')
    age = int(input('Enter age: '))
    clss = int(input("enter class (11-12): "))
    section = input("enter section (A-Z): ")
    stream = 
    transport = input("enter transport (bus or private): ")

    if transport == 'bus':
        bus_no  = int(input("enter bus number: "))
        bus_stop = input("enter bus stop: ")
    else:
        bus_no , bus_stop  = None, None 

    guardian = input("enter name of guardian(s) (each separated by a \' & \'): ")
    tel = input('enter phone number: ')
    email = input('enter email: ')
    address = 
    cpr = input('enter student\'s cpr number: ')

    #to generate new student_id
    cmd = "SELECT MAX(STUDENT_ID) FROM STUDENT"
    cursor.execute(cmd)
    student_id = (cursor.fetchone())[0] + 1

    cmd = "INSERT INTO STUDENT VALUES('{}', '{}', '{}', '{}', {}, {}, '{}', {}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}' )",format(student_id, name, dob, gender, age, clss, section, stream, transport, bus_no, bus_stop, guardian, tel, email, address,cpr)
    cursor.execute(cmd)
    db.commit()
    





