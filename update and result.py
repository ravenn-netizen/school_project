import mysql.connector as sql
db=sql.connect(host='localhost',user='root',password='1922',database='School')
cursor=db.cursor()
gr=int(input("enter gr.no of the student to be updated:"))
def updateclass():
    nclass=int(input("Enter new class of the student:"))
    com="update student set Class='{}' where Grno={}".format(nclass,gr)
    cursor.execute(com)
    db.commit()
def updatebusstop():
    nbusstop=input("Enter new bus stop of the student:")
    com="update student set Busstop='{}' where Grno={}".format(nbusstop,gr)
    cursor.execute(com)
    db.commit()
def updatetel():
    nph=input("Enter new phone number of the student:")
    com="update student set Telephoneno='{}' where Grno={}".format(nph,gr)
    cursor.execute(com)
    db.commit()
while True:
        print("Main Menu:")
        print("1.Class")
        print("2.Bus stop")
        print("3.Telephone number")
        print("4.Exit")
        opt=int(input("Enter option"))
        if opt==1:
            updateclass()
        elif opt==2:
            updatebusstop()
        elif opt==3:
            updatetel()
        elif opt==4:
            break

    
   
            
                    
        
