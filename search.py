import mysql.connector as sql
db=sql.connect(host='localhost',user='root',password='1922',database='School')
cursor=db.cursor()
def search_STUDENTID():
  id=int(input("enter STUDENT_ID"))
  query="select*from student where grno={}".format(id)
  cursor.execute(query)
  rec=cursor.fetchone()
  if rec:
    print("STUDENT_ID=",r[0], "NAME=",r[1], "DOB=",r[2], "GENDER=",r[3], "AGE=",r[4], "GRADE=",r[5], "SECTION=",r[6], "STREAM=",r[7], "TRANSPORT=",r[8], "BUS.NO=",r[9], "BUS STOP=",r[10], "GUARDIAN=",r[11], "TEL=",r[12], "EMAIL=",r[13], "ADDRESS=",r[14], "CPR=",r[15])
  else:
    print("no record found")
def search_class():
  Class=input("enter class")
  query="select*from student where class='{}'".format(Class)
  cursor.execute(query)
  rec=cursor.fetchall()
  if rec:
    for r in rec:
      print("STUDENT_ID=",r[0], "NAME=",r[1], "DOB=",r[2], "GENDER=",r[3], "AGE=",r[4], "GRADE=",r[5], "SECTION=",r[6], "STREAM=",r[7], "TRANSPORT=",r[8], "BUS.NO=",r[9], "BUS STOP=",r[10], "GUARDIAN=",r[11], "TEL=",r[12], "EMAIL=",r[13], "ADDRESS=",r[14], "CPR=",r[15])
  else:
    print("no record found")
def search_name():
  Name=input("enter name")
  query="select*from student where name='{}'".format(Name)
  cursor.execute(query)
  rec=cursor.fetchall()
  if rec:
    for r in rec:
      print("STUDENT_ID=",r[0], "NAME=",r[1], "DOB=",r[2], "GENDER=",r[3], "AGE=",r[4], "GRADE=",r[5], "SECTION=",r[6], "STREAM=",r[7], "TRANSPORT=",r[8], "BUS.NO=",r[9], "BUS STOP=",r[10], "GUARDIAN=",r[11], "TEL=",r[12], "EMAIL=",r[13], "ADDRESS=",r[14], "CPR=",r[15])
  else:
    print("no record found")
def search_stream():
  Stream=input("enter stream")
  query="select*from student where stream='{}'".format(Stream)
  cursor.execute(query)
  rec=cursor.fetchall()
  if rec:
    for r in rec:
      print("STUDENT_ID=",r[0], "NAME=",r[1], "DOB=",r[2], "GENDER=",r[3], "AGE=",r[4], "GRADE=",r[5], "SECTION=",r[6], "STREAM=",r[7], "TRANSPORT=",r[8], "BUS.NO=",r[9], "BUS STOP=",r[10], "GUARDIAN=",r[11], "TEL=",r[12], "EMAIL=",r[13], "ADDRESS=",r[14], "CPR=",r[15])
  else:
    print("no record found")


