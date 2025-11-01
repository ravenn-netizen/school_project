import mysql.connector as sql
db=sql.connect(host='localhost',user='root',password='****',database='School')
cursor=db.cursor()

#update class 
def update_grade():
    gr=input("enter student id of the student to be updated:")
    nclass=int(input("Enter new class of the student (11/12):"))
    com="update student set Grade= {} where Student_id='{}'".format(nclass,gr)
    cursor.execute(com)
    db.commit()

#update bus stop
def update_busstop():
    gr=input("enter student id of the student to be updated:"))
    nbusstop=input("Enter new bus stop of the student:")
    com="update student set Bus_stop='{}' where Student_id ='{}' ".format(nbusstop,gr)
    cursor.execute(com)
    db.commit()

#update bus no
def update_busno():
    gr=int(input("enter student id of the student to be updated:"))
    nbusno=int(input("Enter new bus number:"))
    com="update student set Bus_no={} where Student_id= '{}' ".format(nbusno,gr)
    cursor.execute(com)
    db.commit()
    
#update telephone no
def update_tel():
    gr=int(input("enter student id of the student to be updated:"))
    nph=input("Enter new phone number of the student:")
    com="update student set Tel='{}' where Student_id='{}'".format(nph,gr)
    cursor.execute(com)
    db.commit()

#update staff passwd
def update_staffpass():
    id=input("Enter staffid:")
    npass=input("Enter new password of Staff:")
    com="UPDATE STAFF SET PASSWORD='{}' WHERE STAFFID='{}' ".format(npass,id)
    cursor.execute(com)
    db.commit()

#stream
streams={'H01':('English','Home Science','Psychology','Marketing','Sociology'), 'C01':('English','Accountancy','Business Studies','Economics','Mathematics'),'C02':('English','Accountancy','Business Studies','Economics','Informatics Practices'),'C03':('English','Accountancy','Business Studies','Economics','Marketing'),'S01':( 'English','Physics','Chemistry','Mathematics','Biology'),'S02':('English','Physics','Chemistry','Mathematics','Computer Science'),'S03':('English','Physics','Chemistry','Mathematics','Engineering Graphics'),'S04':('English','Physics','Chemistry','Biology','Computer Science'),'S05':('English','Physics','Chemistry','Biology','Bio-Technology'),'S06':('English','Physics','Chemistry','Mathematics','Artificial Intelligence')}
def stream(stream_code):
    global streams
    if stream_code in streams:
        subject=streams[stream_code]
        sub1,sub2,sub3,sub4,sub5=subject[0],subject[1],subject[2],subject[3],subject[4]
    return sub1,sub2,sub3,sub4,sub5
    
#input marks into table academic
def marksmanagement():
    sid=input("Enter student id:")
    term=input("Enter term:")
    query = "SELECT STREAM FROM STUDENT WHERE STUDENT_ID = '{}'".format(sid)
    cursor.execute(query)
    stream_code = cursor.fetchone()
    s1,s2,s3,s4,s5=stream(stream_code[0])
    s1=int(input("Enter marks of '{}' ".format(s1)))
    s2=int(input("Enter marks of '{}' ".format(s2)))
    s3=int(input("Enter marks of '{}' ".format(s3)))
    s4=int(input("Enter marks of '{}' ".format(s4)))
    s5=int(input("Enter marks of '{}' ".format(s5)))
    avg=(s1+s2+s3+s4+s5)/5
    remark=input("Enter remarks:")
    com="INSERT INTO ACADEMIC VALUES ('{}','{}',{},{},{},{},{},{},'{}')".format (sid,term,s1,s2,s3,s4,s5,avg,remark)
    cursor.execute(com)
    db.commit()


#PROGRESS REPORT
#center() is method used to print the string at the centre of the output screen 
#syntax of center is text.center(width)
def progress_report():
    sid=input("Enter Studend Id of the student: ")
    term= input("Enter term: ")
    print("THE INDIAN SCHOOL, KINGDOM OF BAHRAIN".center(400))
    print("PROGRESS REPORT 2025-2026".center(410))
    print(term.center(450))
    cursor.execute("SELECT * FROM STUDENT WHERE STUDENT_ID='{}' ").format(sid)
    rec=cursor.fetchone()
    if rec:
        gr,name,cl,sec=rec[0],rec[1],rec[5]rec[6]
        print("Student Id : ",gr)
        print("NAME OF STUDENT: ",name)
        print("CLASS AND SECTION : ",cl,sec,sep=' ')
    else:
        print("No record found")


while True:
        print("1.Update grade")
        print("2.Update bus stop")
        print("3.Update bus number")
        print("4.Update telephone")
        print("5.Update staff password ")
        print("6.Delete Student")
        print("7.Exit")
        
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
            update_staffpass()
        elif opt==6:
            del_student()
        elif opt==7:
            break

