import mysql.connector as sql
db=sql.connect(host='localhost',user='root',password='****',database='School')
cursor=db.cursor()

#update class 
def updateclass():
    gr=int(input("enter gr.no of the student to be updated:"))
    nclass=int(input("Enter new class of the student:"))
    com="update student set Class='{}' where Grno={}".format(nclass,gr)
    cursor.execute(com)
    db.commit()

#update bus stop
def updatebusstop():
    gr=int(input("enter gr.no of the student to be updated:"))
    nbusstop=input("Enter new bus stop of the student:")
    com="update student set Busstop='{}' where Grno={}".format(nbusstop,gr)
    cursor.execute(com)
    db.commit()

#update bus no
def updatebusno():
    gr=int(input("enter gr.no of the student to be updated:"))
    nbusno=int(input("Enter new bus number:"))
    com="update student set Busno={} where Grno={}".format(nbusno,gr)
    cursor.execute(com)
    db.commit()
    
#update telephone no
def updatetel():
    gr=int(input("enter gr.no of the student to be updated:"))
    nph=input("Enter new phone number of the student:")
    com="update student set Telephoneno='{}' where Grno={}".format(nph,gr)
    cursor.execute(com)
    db.commit()

#update staff passwd
def updatestaffpass():
    id=input("Enter staffid:")
    npass=input("Enter new password of Staff:")
    com="UPDATE STAFF SET PASSWORD='{}' WHERE STAFFID='{}' ".format(npass,id)
    cursor.execute(com)
    db.commit()

#stream
def stream(stream_code):
    global streams
    streams={'H01':('English','Home Science','Psychology','Marketing','Sociology'), 'C01':('English','Accountancy','Business Studies','Economics','Mathematics'),'C02':('English','Accountancy','Business Studies','Economics',
                        'Informatics Practices'),'C03':('English','Accountancy','Business Studies','Economics','Marketing'),'S01':( 'English','Physics','Chemistry','Mathematics','Biology'),'S02':('English','Physics','Chemistry','Mathematics',
                        'Computer Science'),'S03':('English','Physics','Chemistry','Mathematics','Engineering Graphics'),'S04':('English','Physics','Chemistry','Biology','Computer Science'),'S05':('English','Physics','Chemistry','Biology',
                        'Bio-Technology'),'S06':('English','Physics','Chemistry','Mathematics','Artificial Intelligence')}
    if stream_code in streams:
        subject=streams[stream_code]
        sub1,sub2,sub3,sub4,sub5=subject[0],subject[1],subject[2],subject[3],subject[4]
    return sub1,sub2,sub3,sub4,sub5
    
#input marks into table academic
def marksmanagement():
    sid=input("Enter student id:")
    term=input("Enter term:")
    for stream_code,subject in streams:
        print(stream_code,subject)
    opt=int(input("Enter stream code"))
    print(stream(opt))
    s1,s2,s3,s4,s5=sub1,sub2,sub3,sub4,sub5
    s1=int(input("Enter marks of subject 1 "))
    s2=int(input("Enter marks of subject 2"))
    s3=int(input("Enter marks of subject 3"))
    s4=int(input("Enter marks of subject 4"))
    s5=int(input("Enter marks of subject 5"))
    avg=(s1+s2+s3+s4+s5)/5
    remark=input("Enter remarks:")
    com="INSERT INTO ACADEMIC VALUES ('{}','{}',{},{},{},{},{},{},'{}')".format (sid,term,s1,s2,s3,s4,s5,avg,remark)
    cursor.execute(com)
    db.commit()
    

#PROGRESS REPORT
def progress_report():
    print("THE INDIAN SCHOOL, KINGDOM OF BAHRAIN".center(400))
    print("PROGRESS REPORT 2025-2026".center(410))
    

while True:
    print("Main Menu:")
    print("1.Class")
    print("2.Bus stop")
    print("3.Bus Number")
    print("4.Telephone number")
    print("5.Exit")
    opt=int(input("Enter option"))
    if opt==1:
        updateclass()
    elif opt==2:
        updatebusstop()
    elif opt==3:
        updatebusno()
    elif opt==4:
        updatetel()
    elif opt==5:
        break





