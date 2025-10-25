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
def stream():
    print("MAIN MENU:")
    print("1. Humanities")
    print("2.Business Studies")
    print("3.Informatics Practices")
    print("4.Marketing")
    print("5.Biology")
    print("6.Maths Computer Science")
    print("7.Engineering Graphics")
    print("8.Biology Computer Science")
    print("9.Bio-technology")
    print("10.Artificial Intelligence")
    opt=int(input("Enter option:"))
    if opt==1:
        sub1='English'
        sub2='Home Science'
        sub3='Psychology'
        sub4='Marketing'
        sub5='Sociology'
    elif opt==2:
        sub1='English'
        sub2='Accountancy'
        sub3='Business Studies'
        sub4='Economics'
        sub5='Mathematics'
    elif opt==3:
        sub1='English'
        sub2='Accountancy'
        sub3='Business Studies'
        sub4='Economics'
        sub5='Informatics Practices'
    elif opt==4:
        sub1='English'
        sub2='Accountancy'
        sub3='Business Studies'
        sub4='Economics'
        sub5='Marketing'
    elif opt==5:
        sub1='English'
        sub2='Physics'
        sub3='Chemistry'
        sub4='Mathematics'
        sub5='Biology'
    elif opt==6:
        sub1='English'
        sub2='Physics'
        sub3='Chemistry'
        sub4='Mathematics'
        sub5='Computer Science'
    elif opt==7:
        sub1='English'
        sub2='Physics'
        sub3='Chemistry'
        sub4='Mathematics'
        sub5='Engineering Graphics'
    elif opt==8:
        sub1='English'
        sub2='Physics'
        sub3='Chemistry'
        sub4='Biology'
        sub5='Computer Science'
    elif opt==9:
        sub1='English'
        sub2='Physics'
        sub3='Chemistry'
        sub4='Biology'
        sub5='Bio-Technology'
    elif opt==10:
        sub1='English'
        sub2='Physics'
        sub3='Chemistry'
        sub4='Mathematics'
        sub5='Artificial Intelligence'
    return sub1,sub2,sub3,sub4,sub5

#input marks into table academic
def marksmanagement():
    sid=input("Enter student id:")
    term=input("Enter term:")
    print(stream())
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



