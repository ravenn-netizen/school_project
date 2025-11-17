#to establish python-sql connection

import mysql.connector as sql
db = sql.connect(host='localhost', user='root', passwd='****')
cursor = db.cursor()
from tabulate import tabulate


#to create database
def createdb():
    cmd= "CREATE DATABASE SCHOOL"
    cursor.execute(cmd)
    cmd= "USE SCHOOL"
    cursor.execute(cmd)

#to create table 'STUDENT'
def createTableStudent():
    cursor.execute(cmd)
    cmd="CREATE TABLE STUDENT(STUDENT_ID INT PRIMARY KEY, NAME VARCHAR(200), DOB DATE, GENDER CHAR(1), AGE INT, GRADE INT, SECTION CHAR(1), STREAM CHAR(3), TRANSPORT VARCHAR(10), BUS_NO INT, BUS_STOP VARCHAR(40), GUARDIAN TEXT, TEL CHAR(8), EMAIL VARCHAR(60), ADDRESS TEXT , CPR VARCHAR(9), PASSWORD VARCHAR(30))"
    cursor.execute(cmd)

#to create table 'ACADEMIC'
def createTableAcademic():
    cmd= "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "CREATE TABLE ACADEMIC(SNO INT PRIMARY KEY, STUDENT_ID INT, TERM VARCHAR(6), SUB1 FLOAT, SUB2 FLOAT, SUB3 FLOAT, SUB4 FLOAT, SUB5 FLOAT, AVG FLOAT, REMARKS varchar(10) )"
    cursor.execute(cmd)

#to create table 'STAFF'
def createTableStaff():
    cursor.execute(cmd)
    cmd = "CREATE TABLE STAFF(STAFF_ID INT PRIMARY KEY, NAME VARCHAR(200), DEPARTMENT VARCHAR(20), CPR VARCHAR(9), PASSWORD VARCHAR(30))"
    cursor.execute(cmd)

#to create table 'ANNOUNCEMENT'
def createTableAnnouncement():
    cursor.execute(cmd)
    cmd = "CREATE TABLE ANNOUNCEMENT(REF INT PRIMARY KEY, SENDER INT, RECEIPIENT_TYPE varchar(20), RECEIPIENT varchar(20), DATE date, SUBJECT TEXT, CONTENT text)"
    cursor.execute(cmd)

cursor.execute('use school')

streams={'H01':('English','Home Science','Psychology','Marketing','Sociology'), 'C01':('English','Accountancy','Business Studies','Economics','Mathematics'),'C02':('English','Accountancy','Business Studies','Economics','Informatics Practices'),'C03':('English','Accountancy','Business Studies','Economics','Marketing'),'S01':( 'English','Physics','Chemistry','Mathematics','Biology'),'S02':('English','Physics','Chemistry','Mathematics','Computer Science'),'S03':('English','Physics','Chemistry','Mathematics','Engineering Graphics'),'S04':('English','Physics','Chemistry','Biology','Computer Science'),'S05':('English','Physics','Chemistry','Biology','Bio-Technology'),'S06':('English','Physics','Chemistry','Mathematics','Artificial Intelligence')}

def new_student():

    name = input("enter name: ").title()
    dob = input('enter date of birth YYYY-MM-DD: ')
    gender = input('enter gender (M or F): ').upper().strip()

    age = int(input('Enter age: '))
    grade = int(input("enter class (11-12): "))
    section = input("enter section (A-Z): ").upper()
    
    # see guys i made a global dictionary that contain streamcode (eg: H01, C02, S03) and corresponding subjects
    # now im printing the streamcode and its subjects to let the staff confirm that their entering the right stream code
    print()
    for stream_code, subjects in streams.items():
        print(stream_code, subjects)
    print()    
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
    address = input('enter address (eg: Flat: 1, Bldg: 1048, Road: 1318, Block: 113, Area: Hidd):  ')
    cpr = input('enter student\'s cpr number: ').strip()

    #to generate new student_id
    cmd = "SELECT MAX(STUDENT_ID) FROM STUDENT"
    cursor.execute(cmd)
    result = cursor.fetchone()
    
    if not result:
        student_id = 1
    else:
        student_id = result[0] + 1
#password is set default to password until changed by the student
    password = 'password'
    print('Generated student id is', student_id, '\n')
    
    cmd = "INSERT INTO STUDENT VALUES({}, '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}' ,'{}')".format(student_id, name, dob, gender, age, grade, section, stream, transport, bus_no, bus_stop, guardian, tel, email, address,cpr, password)
    cursor.execute(cmd)
    db.commit()


def new_staff():
    #usr inputs details
    cpr = input('enter cpr: ')
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

def staff_sign_in():
    # to enter staff id and check if in database
    
    while True:
        staff_id =int(input('enter staff id: '))
        cmd = 'SELECT STAFF_ID FROM STAFF'
        cursor.execute(cmd)
        records = cursor.fetchall()

        if (staff_id,) in records:
            break
        else:
            print(records)
            print('\nstaff id entered does not exist')
            print('1. try again')
            print('2. exit to main menu\n')
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
            print("Hello, staff '{}'".format(staff_id))
            print("Welcome to the database.\n")
            return staff_id
        else: 
            print('\nwrong password')
            print('1. try password again')
            print('2. exit to main menu\n')
            opt = int(input('enter option: '))
            if opt == 1:
                continue
            if opt == 2:
                return 0
    
def student_sign_in():
    
    while True:
        student_id = int(input('enter student id: '))
        cmd = 'SELECT STUDENT_ID FROM STUDENT'
        cursor.execute(cmd)
        records = cursor.fetchall()
        if (student_id,) in records:
            break
        else:
            print('\nstudent id entered does not exist')
            print('1. try again')
            print('2. exit to main menu\n')
            opt = int(input('enter option: '))

            if opt == 1:
                continue
            elif opt == 2:
                return 0
    
    cmd = "SELECT PASSWORD FROM STUDENT WHERE STUDENT_ID = '{}'".format(student_id)
    cursor.execute(cmd)
    password_in_db = cursor.fetchone()[0]

    while True: 
        entered_password = input('enter password: ')
        if entered_password == password_in_db:
            print('Hello, student "{}"!'.format(student_id))
            print('Welcome to the database.\n')
            return student_id
        else: 
            print('\nwrong password')
            print('1. try password again')
            print('2. exit to main menu\n')
            opt = int(input('enter option: '))
            if opt == 1:
                continue
            if opt == 2:
                return 0

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
                      
def search_STUDENTID():
    
    id = int(input("Enter student id: "))
    query = "SELECT * FROM student WHERE STUDENT_ID = {}".format(id)
    cursor.execute(query)
    rec = cursor.fetchone()
    if rec:
        headers = ["STUDENT_ID","NAME","DOB","GENDER","AGE","GRADE","SECTION","STREAM",
                   "TRANSPORT","BUS.NO","BUS STOP","GUARDIAN","TEL","EMAIL","ADDRESS","CPR"]
        table = [rec]
        print(tabulate(table, headers=headers, tablefmt="psql"))
    else:
        print("No record found")
        
def search_class():
    
    cl = input("Enter class: ").upper()
    sec = input("Enter section: ").upper()
    query = "SELECT * FROM student WHERE grade = {} and section='{}'".format(cl, sec)
    cursor.execute(query)
    rec = cursor.fetchall()
    if rec:
        headers = ["STUDENT_ID","NAME","DOB","GENDER","AGE","GRADE","SECTION","STREAM",
                   "TRANSPORT","BUS.NO","BUS STOP","GUARDIAN","TEL","EMAIL","ADDRESS","CPR"]
        print(tabulate(rec, headers=headers, tablefmt="psql"))
    else:
        print("No record found")
        
def search_name():
    
    Name = input("Enter name: ").title()
    query = "SELECT * FROM student WHERE name = '{}'".format(Name)
    cursor.execute(query)
    rec = cursor.fetchall()
    if rec:
        headers = ["STUDENT_ID","NAME","DOB","GENDER","AGE","GRADE","SECTION","STREAM",
                   "TRANSPORT","BUS.NO","BUS STOP","GUARDIAN","TEL","EMAIL","ADDRESS","CPR"]
        print(tabulate(rec, headers=headers, tablefmt="psql"))
    else:
        print("No record found")
        
def search_stream():
    
    Stream = input("Enter stream: ")
    query = "SELECT * FROM student WHERE stream = '{}'".format(Stream)
    cursor.execute(query)
    rec = cursor.fetchall()
    if rec:
        headers = ["STUDENT_ID","NAME","DOB","GENDER","AGE","GRADE","SECTION","STREAM",
                   "TRANSPORT","BUS.NO","BUS STOP","GUARDIAN","TEL","EMAIL","ADDRESS","CPR"]
        print(tabulate(rec, headers=headers, tablefmt="psql"))
    else:
        print("No record found")

def search():
    while True:
        print("\n--- Search Menu ---\n")
        print('1. student id')
        print('2. class')
        print('3. name')
        print('4. stream')
        print('5. exit to menu\n')
        opt = int(input('Enter option: '))
        if opt ==1:
            search_STUDENTID()
        if opt == 2:
            search_class()
        if opt == 3:
            search_name()
        elif opt == 4:
            search_stream()
        elif opt ==5:
            return 0
        else:
            print('Enter valid option.\n')

def report_group_by_section():
    grade = int(input('enter grade (11/12): '))
    term = input("enter term ('first', 'second' or 'third'): ").lower()
    query = "SELECT S.GRADE, S.SECTION, COUNT(A.STUDENT_ID), AVG(A.AVG), MIN(A.AVG), MAX(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE = {} AND A.TERM= '{}' GROUP BY S.SECTION ORDER BY S.SECTION".format(grade, term)
    cursor.execute(query)
    records = cursor.fetchall()

    if not records: #if no records found this statement is true and escapes the function
                print('No records found corresponding to entered grade')
                return 0
            
    table_headers = ['Grade','Section', 'No. of students', 'Class average', 'Class minimum', 'Class maximum']
    print(tabulate(records, headers =table_headers, tablefmt="psql"))

#unread value error in this function, dk why
def report_specific_section():
    grade = int(input('enter grade (11/12): '))
    section = input("enter section: ").upper()
    term = input("enter term ('first', 'second' or 'third'): ").lower()
    query = "SELECT NAME, S.STUDENT_ID, A.SUB1, A.SUB2, A.SUB3, A.SUB4, A.SUB5, A.AVG, A.REMARKS FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE={} AND S.SECTION='{}' AND A.TERM ='{}' ORDER BY S.NAME".format(grade, section, term)
    cursor.execute(query)
    records = cursor.fetchall()

    if not records: #''
                print('No records found corresponding to entered grade and/or section')
                return 0
    
    query = "SELECT STREAM FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE = {} AND S.SECTION = '{}' AND A.TERM='{}'".format(grade, section, term)
    cursor.execute(query)
    stream_code = cursor.fetchone()[0]
    sub1, sub2, sub3, sub4, sub5 = streams[stream_code]

    
    table_headers =['NAME', 'STUDENT_ID', sub1, sub2, sub3, sub4, sub5, 'AVERAGE', 'REMARK']
    print(tabulate(records, headers=table_headers, tablefmt = 'grid'))
    print()
    
    query = "SELECT COUNT(S.STUDENT_ID), MIN(A.AVG) , MAX(A.AVG), AVG(A.AVG)  FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE={} AND S.SECTION='{}' AND A.TERM='{}' ".format(grade, section, term)
    cursor.execute(query)
    rec= cursor.fetchone()
    if not rec: 
                print('No records found corresponding to entered credentials')
                return 0
            
    print('Number of students enrolled:', rec[0])
    print('Class average score:', rec[1])
    print('Class minimum score:', rec[2])
    print('Class maximum score:', rec[3])
    print()
    
def report_group_by_stream():
    grade = int(input('Enter grade (11/12): '))
    term = input("enter term ('first', 'second' or 'third'): ").lower()
    query = "SELECT S.STREAM, COUNT(A.STUDENT_ID), MIN(A.AVG), MAX(A.AVG), AVG(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE={} AND A.TERM = '{}' GROUP BY S.STREAM ORDER BY S.STREAM".format(grade, term)
    cursor.execute(query)
    recs = cursor.fetchall()
    
    if not recs:
                print('No records found corresponding to entered credentials')
                return 0
    for rec in recs:
        print('Stream:', rec[0])
        print('Number of students enrolled:', rec[1])
        print('Minimum score:', rec[2])
        print('Maximum score:', rec[3])
        print('Average score:', rec[4])
        print()
    
def report_specific_stream():
    grade = int(input('enter grade (11/12): '))
    term = input("enter term ('first', 'second' or 'third'): \n").lower()
    global streams
    
    for stream_code in streams:
        print(stream_code, streams[stream_code])
    print()
    stream_code = input('enter stream code: ')
    if stream_code not in streams:
        print('Invalid stream code')
        return 0
    i=1        
    for subject in streams[stream_code]:
        sub = 'SUB'+str(i)
        query = "SELECT MIN(A.{}), MAX(A.{}), AVG(A.{}) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.STREAM ='{}' AND A.TERM='{}' AND S.GRADE={}".format(sub, sub, sub, stream_code, term, grade)  
        cursor.execute(query)
        rec = cursor.fetchone()
        if not rec:
                print('No records found corresponding to entered credentials')
                return 0
        print(subject)
        print('Minimum score:', rec[0])
        print('Maximum score:', rec[1])
        print('Average score:', rec[2])
        print()
        i+=1
            
    query = "SELECT  COUNT(S.STUDENT_ID), AVG(A.AVG), MIN(A.AVG), MAX(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.STREAM='{}'  AND A.TERM ='{}' AND GRADE={}".format(stream_code, term, grade)
    cursor.execute(query)
    rec = cursor.fetchone()
    if not rec:
        print('No records found corresponding to entered credentials\n')
        return 0
                
    print('Number of students enrolled:', rec[0])
    print('Minimum score:', rec[1])
    print('Maximum score:', rec[2])
    print('Average score:', rec[3])
    print()
    
def report():
    while True:
        print('\n---REPORT MENU---\n')
        print("1. group by section")
        print("2. specific section")
        print("3. group by stream")
        print("4. specific stream")
        print("5. exit\n")
        opt = int(input("enter option: "))

        if opt == 1:
            report_group_by_section()    
        elif opt == 2:
            report_specific_section()
        elif opt == 3:
            report_group_by_stream()
        elif opt == 4:
            report_specific_stream()
        elif opt ==5:
            return 0


#update class 
def update_grade():
    gr=int(input("Enter student id of the student to be updated:"))
    nclass=int(input("Enter new class of the student (11/12):"))
    com="update student set Grade= {} where Student_id='{}'".format(nclass,gr)
    cursor.execute(com)
    db.commit()

#update bus stop
def update_busstop():
    gr=int(input("Enter student id of the student to be updated:"))
    nbusstop=input("Enter new bus stop of the student:").lower()
    com="update student set Bus_stop='{}' where Student_id ={} ".format(nbusstop,gr)
    cursor.execute(com)
    db.commit()

#update bus no
def update_busno():
    gr=int(input("enter student id of the student to be updated:"))
    nbusno=int(input("Enter new bus number:"))
    com="update student set Bus_no={} where Student_id= {} ".format(nbusno,gr)
    cursor.execute(com)
    db.commit()
    
#update telephone no
def update_tel():
    gr=int(input("enter student id of the student to be updated:"))
    nph=input("Enter new phone number of the student:")
    com="update student set Tel='{}' where Student_id={}".format(nph,gr)
    cursor.execute(com)
    db.commit()

#update staff passwd
def update_staffpass():
    staff_id=int(input("Enter staffid:"))
    npass=input("Enter new password of Staff:")
    com="UPDATE STAFF SET PASSWORD='{}' WHERE STAFFID={} ".format(npass,staff_id)
    cursor.execute(com)
    db.commit()

#update student password
def update_studentpass():
    gr=int(input("Enter student id of the student to be updated:"))
    npass=input("Enter new password of the student:")
    com="UPDATE STUDENT SET PASSWORD = '{}' WHERE STUDENT_ID={}". format(npass,gr)
    cursor.execute(com)
    db.commit()

#delete student record
def del_student():
    gr=int(input("Enter student id of student to be removed:"))
    com="Delete from Student where Student_id = {} ".format(gr)
    com1="Delete from Academic where Studentid = {} ".format(gr)
    cursor.execute(com)
    cursor.execute(com1)
    db.commit()
#even if the entered id is not present in either or one of them it doesn't show any error

def update_student_info_menu():
    while True:
            print('\n--- Update Menu ---\n')
            print("1.Update grade")
            print("2.Update bus stop")
            print("3.Update bus number")
            print("4.Update telephone")
            print("5.Delete Student")
            print("6.Exit\n")
            
            opt=int(input("Enter option"))
            if opt==1:
                update_grade()
            elif opt==2:
                update_busstop()
            elif opt==3:
                update_busno()
            elif opt==4:
                update_tel()
            elif opt==5:
                del_student()
            elif opt==6:
                break

    
#input marks into table academic
def marksmanagement():
    n=int(input("Enter no. of inputs: "))
    for i in range (n):
        sid=int(input("Enter student id:"))
        term=input("Enter term:").upper()
        query = "SELECT STREAM FROM STUDENT WHERE STUDENT_ID = {}".format(sid)
        cursor.execute(query)
        rec = cursor.fetchone()
        for stream_code,subject in streams.items():
            print(stream_code,subject)
        opt = input("Enter subject code:").upper()
        print(stream(opt))
        s1=int(input("Enter marks of subject 1:"))
        s2=int(input("Enter marks of subject 2:"))
        s3=int(input("Enter marks of subject 3:"))
        s4=int(input("Enter marks of subject 4:"))
        s5=int(input("Enter marks of subject 5:"))
        avg=(s1+s2+s3+s4+s5)/5
        remark=input("Enter remarks:").upper()
        
        cmd = "SELECT MAX(SNO) FROM ACADEMIC"
        cursor.execute(cmd)
        result = cursor.fetchone()
        if not result:
            new_sno=1
        else:
            new_sno=result[0]+1
        
        com="INSERT INTO ACADEMIC VALUES ({}, {},'{}',{},{},{},{},{},{},'{}')".format (new_sno, sid,term,s1,s2,s3,s4,s5,avg,remark)
        cursor.execute(com)
        db.commit()
#PROGRESS REPORT
#center() is method used to print the string at the centre of the output screen 
#syntax of center is text.center(width)
def progress_report(student_id):
    sid = student_id
    term= input("Enter term: ").upper()
    nterm=term+' '+'TERM'  
    #to display like "FIRST TERM" in the report card
    #made it as nterm as term is later used in the code to fetch data from student table
    print("THE INDIAN SCHOOL, KINGDOM OF BAHRAIN".center(400))
    print("PROGRESS REPORT 2025-2026".center(410))
    print(nterm.center(445))
    cmd="SELECT * FROM STUDENT WHERE STUDENT_ID={}".format(sid)
    cursor.execute(cmd)
    rec=cursor.fetchone()
    #rec contains the record of student from the table student
    if rec:
        gr,name,cl,sec=rec[0],rec[1],rec[5],rec[6]
        print("Student Id : ",gr)
        print("NAME OF STUDENT: ",name)
        print("CLASS AND SECTION : ",cl,sec,sep=' ')
        #to select rec from academic
        cmd1="SELECT * FROM ACADEMIC WHERE STUDENT_ID = {} AND TERM='{}' ".format(sid,term)
        cursor.execute(cmd1)
        rec1= cursor.fetchone()
        #rec1 contains record of student from the table academic
       
        #to select the stream of the student from the table student 
        opt=rec[7]           
        s1,s2,s3,s4,s5=streams[opt]
        data=[[s1,rec1[3]],[s2,rec1[4]],[s3,rec1[5]],[s4,rec1[6]],[s5,rec1[7]]] 
        #data will be now like [[sub1,mark],[sub2,mark],etc]
        header=['SUBJECT','MARKS']
        print(tabulate (data,headers=header,tablefmt='grid'))
        print("AVERAGE:",rec1[-2])
        print("REMARKS:",rec1[-1])
    else:
        print("No record found")


def send_announcement(staff_id):
    sender = staff_id

    #to input receiver and their type
    print('choose receiver type')
    print('1. grade')
    print('2. section')
    print('3. student')
    opt = int(input('enter option: '))
    if opt==1:
        receipient_type = 'grade'
        receipient = input('enter grade: ')
    elif opt==2:
        receipient_type  = 'section'
        receipient = input('enter grade and section (grade&section): ')
    elif opt==3:
        receipient_type = 'student'
        receipient = input('enter id: ')

    # to create reference for announcement
    cmd = "SELECT MAX(REF) FROM ANNOUNCEMENT"
    cursor.execute(cmd)
    result = cursor.fetchone()
    
    if not result:
        ref = 1
    else:
        ref = result[0] + 1

    #to input announcement content
    date = input('enter date YYYY-MM-DD: ')
    subject = input('enter subject: ')
    content = input('enter content: ')
    
    #to add into to file 
    cmd = "INSERT INTO ANNOUNCEMENT VALUES({}, {}, '{}', '{}', '{}','{}', '{}')".format(ref, sender, receipient_type, receipient, date, subject, content)
    cursor.execute(cmd)

    db.commit()

def received_announcement(student_id):

    #to check for announcements for user and add to their inbox 
    cmd = "SELECT GRADE, SECTION FROM STUDENT WHERE STUDENT_ID={}".format(student_id)
    cursor.execute(cmd)
    grade, section = cursor.fetchone()
    
    cmd = "SELECT * FROM ANNOUNCEMENT"
    cursor.execute(cmd)
    records = cursor.fetchall()

    if not records :
        print('No announcements in inbox')
        print('Check another time :)\n')
        return 0

    inbox=[]
    for record in records:

        receipient_type = record[2]
        receipient = record[3]
        if receipient_type == 'grade' and int(receipient) == grade:
            inbox.append(record)

        elif receipient_type == 'section':
            receipient = receipient.split('&')

            if int(receipient[0])== grade and receipient[1] == section:
                inbox.append(record)

        elif receipient_type == 'student':
            if int(receipient) == student_id:
                inbox.append(record)

    #to open each message
    print('announcements in inbox:', len(inbox))
    if not inbox:
        print('No announcement in inbox')
        print('Check another time :)\n')
        return 0

    if len(inbox):
        i=0
        for record in records:
            i+=1
            print(str(i)+'.', record[-2])  #here record[-2] is the subject of the announcement

            while True:

                print('\nEnter 0 for option to exit')
                opt = int(input('enter message to open: '))
                if opt == 0:
                    return 0                
                elif opt > len(inbox) :  #to check if entered optionis within range; if not loops over
                    print('enter valid option')
                    continue 

                message = inbox[opt-1]
                
                #to find sending staff's name as only their staff_id is stored in the table    
                cmd = "SELECT NAME FROM STAFF WHERE STAFF_ID = {}".format(message[1])
                cursor.execute(cmd)
                sender_name = cursor.fetchone()[0]
                print('FROM:', sender_name, '\n')
                print('SUBJECT:', message[-2], '\n')
                print('CONTENT:', '\n', message[-1], '\n')

    else:
        print('No announcement in inbox')
        print('Check another time :)')

def Main_Menu():
    while True:
        print("\n--- School Management System ---\n")
        print("1. Admin Sign In")
        print("2. Staff Sign In")
        print("3. Student Sign In")
        print("4. Exit\n")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            if admin_sign_in():
                admin_menu()
        elif choice == '2':
            staff_id = staff_sign_in()
            if staff_id != 0:
                staff_menu(staff_id)
        elif choice == '3':
            student_id = student_sign_in()
            if student_id != 0:
                student_menu(student_id)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
            
def admin_menu():
    print("\n--- Admin Menu ---\n")
    print("1. staff management")
    print("2. student management\n")

    opt = int(input("enter option: "))

    if opt == 1:
        print('Add New Staff')
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
            
def staff_menu(staff_id):
    while True:
        print("\n--- Staff Menu ---\n")
        print("1. Student Management")
        print("2. Send Announcement")
        print("3. Reports")
        print("4. Update my Password")
        print("5. Logout\n")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            while True:
                print("\n--- Student Info ---")
                print("a. New Admission")
                print("b. Search Student")
                print("c. Marks Management")
                print("d. Update Student Info")
                print("e. Remove Student")
                print("f. Back to Staff Menu\n")
                sub_choice = input("Select option (a-f): ").lower()

                #functions based on sub_choice
                if sub_choice == 'a':
                    new_student()
                elif sub_choice == 'b':
                    search()
                elif sub_choice == 'c':
                    marksmanagement()
                elif sub_choice == 'd':
                    update_student_info_menu()
                elif sub_choice == 'e':
                    del_student()
                elif sub_choice == 'f':
                    break
                else:
                    print("Invalid option, please try again.")
                    
        elif choice == '2':
            send_announcement(staff_id)
        elif choice == '3':
            report()
        elif choice == '4':
            update_staff_pass()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice!")


def student_menu(student_id):
    while True:
        print("\n--- Student Menu ---\n")
        print("1. View Announcements")
        print("2. View Result")
        print("3. Update Password")
        print("4. Logout\n")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            received_announcement(student_id)
        elif choice == '2':
            progress_report(student_id)
        elif choice == '3':
            update_studentpass()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice!")
    

Main_Menu()
