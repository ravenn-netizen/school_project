def new_admission():
    name = input("enter name: ").title()
    dob = input('enter date of birth YYYY-MM-DD: ')
    gender = input('enter gender (M or F): ').upper().strip()
    age = int(input('Enter age: '))
    grade = int(input("enter class (11-12): "))
    section = input("enter section (A-Z): ").upper()
    # see guys i made a global dictionary that contain streamcode (eg: H01, C02, S03) and corresponding subjects
    # now im print the streamcode and its subjects to let the staff confirm that their entering the right stream code
    for stream_code, subjects in streams:
        print(stream_code, subjects)
        
    stream = input("enter stream: ")
    transport = input("enter transport (bus or private): ").lower().strip()

    if transport == 'bus':
        bus_no  = int(input("enter bus number: "))
        bus_stop = input("enter bus stop: ").lower()
    else:
        bus_no , bus_stop  = None, None 

    guardian = input("enter name of guardian(s) (each separated by a \' & \'): ").capitalize()
    tel = input('enter phone number: ')
    email = input('enter email: ')
    address = input('enter address ( [flat] & [building] & [road] & [block] & [area] ')
    cpr = input('enter student\'s cpr number: ')

    #to generate new student_id
    cmd = "SELECT MAX(STUDENT_ID) FROM STUDENT"
    cursor.execute(cmd)
    result = cursor.fetchone()
    
    if result is not None:
        i = int(result[0][1:]) +1 
        student_id = 'S'+str(i)
    else:
        student_id = 'S0'
    

    cmd = "INSERT INTO STUDENT VALUES('{}', '{}', '{}', '{}', {}, {}, '{}', {}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}' )",format(student_id, name, dob, gender, age, grade, section, stream, transport, bus_no, bus_stop, guardian, tel, email, address,cpr)
    cursor.execute(cmd)
    db.commit()
    











