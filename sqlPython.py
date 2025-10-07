import mysql.connector as sql
db = sql.connect(host='localhost', user='root', passwd='7563')
cursor = db.cursor()
def createdb(dbname):
    com = "create database {}".format(dbname)
    cursor.execute(com)

def createtable():
    cursor.execute("use bankdb")
    com = "create table bank(accno int primary key, accname varchar(20), balamt float)"
    cursor.execute(com)

def altertable(att, dtype, constraint = 'null' ):
    cursor.execute('use bankdb')
    com = "alter table bank add {} {} {}".format(att, dtype, constraint)
    cursor.execute(com)

def addcustomer():
    cursor.execute('use bankdb')
    accno = int(input('accno: '))
    accname = input('accname: ')
    bal = int(input('balance amount: '))
    address = input('address: ')
    com = "insert into bank values({}, '{}', {}, '{}')".format(accno, accname, bal, address)
    cursor.execute(com)
    db.commit()

addcustomer()
altertable()
createdb()

# yes it works lol YASSS


