import mysql.connector as sql
db=sql.connect(host='localhost',user='root',password='1922',database='School')
cursor=db.cursor()
def search_grno():
  Gr=int(input("enter grno"))
  query="select*from student where grno={}".format(Gr)
  cursor.execute(query)
  rec=cursor.fetchone()
  if rec:
    print("Grnno="rec[0],"class="rec[1],"name="rec[2],"stream="rec[3],"house"=rec[4])
  else:
    print("no record found")
def search_class():
  Class=input("enter class")
  query="select*from student where class='{}'".format(Class)
  cursor.execute(query)
  rec=cursor.fetchall()
  if rec:
    for r in rec:
      print("Grnno="r[0],"class="r[1],"name="r[2],"stream="r[3],"house"=r[4])
  else:
    print("no record found")
def search_name():
  Name=input("enter name")
  query="select*from student where name='{}'".format(Name)
  cursor.execute(query)
  rec=cursor.fetchall()
  if rec:
    for r in rec:
      print("Grnno="r[0],"class="r[1],"name="r[2],"stream="r[3],"house"=r[4])
  else:
    print("no record found")
def search_stream():
  Stream=input("enter stream")
  query="select*from student where stream='{}'".format(Stream)
  cursor.execute(query)
  rec=cursor.fetchall()
  if rec:
    for r in rec:
      print("Grnno="r[0],"class="r[1],"name="r[2],"stream="r[3],"house"=r[4])
  else:
    print("no record found")
def search_house():
  House=input("enter house")
  query="select*from student where house='{}'".format(House)
  cursor.execute(query)
  rec=cursor.fetchall()
  if rec:
    for r in rec:
      print("Grnno="r[0],"class="r[1],"name="r[2],"stream="r[3],"house"=r[4])
  else:
    print("no record found")


