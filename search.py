from tabulate import tabulate
import mysql.connector as sql
db = sql.connect(host='localhost', user='root', password='1922', database='School')
cursor = db.cursor()
def search_STUDENTID():
    id = int(input("Enter STUDENT_ID: "))
    query = "SELECT * FROM student WHERE STUDENT_ID = {}".format(id)
    cursor.execute(query)
    rec = cursor.fetchone()
    if rec:
        headers = ["STUDENT_ID","NAME","DOB","GENDER","AGE","GRADE","SECTION","STREAM",
                   "TRANSPORT","BUS.NO","BUS STOP","GUARDIAN","TEL","EMAIL","ADDRESS","CPR"]
        table = [rec]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No record found")
def search_class():
    Class = input("Enter class: ")
    query = "SELECT * FROM student WHERE class = '{}'".format(Class)
    cursor.execute(query)
    rec = cursor.fetchall()
    if rec:
        headers = ["STUDENT_ID","NAME","DOB","GENDER","AGE","GRADE","SECTION","STREAM",
                   "TRANSPORT","BUS.NO","BUS STOP","GUARDIAN","TEL","EMAIL","ADDRESS","CPR"]
        print(tabulate(rec, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No record found")
def search_name():
    Name = input("Enter name: ")
    query = "SELECT * FROM student WHERE name = '{}'".format(Name)
    cursor.execute(query)
    rec = cursor.fetchall()
    if rec:
        headers = ["STUDENT_ID","NAME","DOB","GENDER","AGE","GRADE","SECTION","STREAM",
                   "TRANSPORT","BUS.NO","BUS STOP","GUARDIAN","TEL","EMAIL","ADDRESS","CPR"]
        print(tabulate(rec, headers=headers, tablefmt="fancy_grid"))
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
        print(tabulate(rec, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No record found")
