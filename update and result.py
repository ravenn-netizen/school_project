import mysql.connector as sql
db=sql.connect(host='localhost',user='root',password='1922',database='School')
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
    com="UPDATE STAFF
    
    


#result 
def result_management():
    

    
        


   
            
                    
        











