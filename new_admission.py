def new_admission():
    name = input("enter name: ").title()
    dob = input('enter date of birth YYYY-MM-DD: ')
    gender = input('enter gender (M or F): ').upper().strip()

    age = int(input('Enter age: '))
    grade = int(input("enter class (11-12): "))
    section = input("enter section (A-Z): ").upper()
    
    # see guys i made a global dictionary that contain streamcode (eg: H01, C02, S03) and corresponding subjects
    # now im print the streamcode and its subjects to let the staff confirm that their entering the right stream code
    streams={'H01':('English','Home Science','Psychology','Marketing','Sociology'), 'C01':('English','Accountancy','Business Studies','Economics','Mathematics'),'C02':('English','Accountancy','Business Studies','Economics','Informatics Practices'),'C03':('English','Accountancy','Business Studies','Economics','Marketing'),'S01':( 'English','Physics','Chemistry','Mathematics','Biology'),'S02':('English','Physics','Chemistry','Mathematics','Computer Science'),'S03':('English','Physics','Chemistry','Mathematics','Engineering Graphics'),'S04':('English','Physics','Chemistry','Biology','Computer Science'),'S05':('English','Physics','Chemistry','Biology','Bio-Technology'),'S06':('English','Physics','Chemistry','Mathematics','Artificial Intelligence')}
    for stream_code, subjects in streams.items():
        print(stream_code, subjects)
        
    stream = input("enter streamcode: ").upper().strip()
    transport = input("enter transport (bus or private): ").lower().strip()

    if transport == 'bus':
        bus_no  = int(input("enter bus number: "))
        bus_stop = input("enter bus stop: ").lower()
    else:
        bus_no , bus_stop  = 0, 'None' 

    guardian = input("enter name of guardian(s) (each separated by a \' & \'): ").capitalize()
    tel = input('enter phone number: ')
    email = input('enter email: ')
    address = input('enter address ( [flat] & [building] & [road] & [block] & [area] ')
    cpr = input('enter student\'s cpr number: ')

    #to generate new student_id
    cmd = "SELECT MAX(STUDENT_ID) FROM STUDENT"
    cursor.execute(cmd)
    result = cursor.fetchone()
    
    if result[0] is None:
        #this is in case the table is empty, so we are entering the first student id ie S0
        student_id = 'S0'
    else:
        i = int(result[0][1:]) +1 
        student_id = 'S'+ str(i)
        #this is in case there are already some records inthe table
        # result[0] to access the id, cuz sql returns it in a tuple
        # result[0][1:] using slicing t extraxt the numerical part; then converting it into int(), then adding +1 to generate a new one
        # for new id convert into string, concatenate to S, AND VOILA! NEW STUDENT ID GUYSS!!
        #this code is cryptic aff ikk so lmk if you can find something simpler
    password = 'password'
    
    cmd = "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "INSERT INTO STUDENT VALUES('{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}' ,'{}')".format(student_id, name, dob, gender, age, grade, section, stream, transport, bus_no, bus_stop, guardian, tel, email, address,cpr, password)
    cursor.execute(cmd)
    db.commit()





