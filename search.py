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
    cl = input("Enter class: ")
    query = "SELECT * FROM student WHERE grade = '{}'".format(cl)
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


##EDITED VERSION AS IN THE COMPILED FILE 
#search_class() is changed to take in sec as an input as well to display students of particular class and section
#title(), upper()and similar string operations made to make sure compliance with data in the database 
#menu created 

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
