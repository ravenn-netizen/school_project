#under improvisation
#finished testing

import mysql.connector as sql
db = sql.connect(host='localhost', user='root', passwd='7563', database='school')
cursor = db.cursor()

from tabulate import tabulate

streams={'H01':('English','Home Science','Psychology','Marketing','Sociology'), 'C01':('English','Accountancy','Business Studies','Economics','Mathematics'),'C02':('English','Accountancy','Business Studies','Economics','Informatics Practices'),'C03':('English','Accountancy','Business Studies','Economics','Marketing'),'S01':( 'English','Physics','Chemistry','Mathematics','Biology'),'S02':('English','Physics','Chemistry','Mathematics','Computer Science'),'S03':('English','Physics','Chemistry','Mathematics','Engineering Graphics'),'S04':('English','Physics','Chemistry','Biology','Computer Science'),'S05':('English','Physics','Chemistry','Biology','Bio-Technology'),'S06':('English','Physics','Chemistry','Mathematics','Artificial Intelligence')}

def stream(stream_code):
    global streams
    if stream_code in streams:
        subject=streams[stream_code]
        sub1,sub2,sub3,sub4,sub5=subject[0],subject[1],subject[2],subject[3],subject[4]
    return sub1,sub2,sub3,sub4,sub5
    
def report_group_by_section():
    grade = int(input('enter grade: '))
    query = "SELECT S.GRADE, S.SECTION, COUNT(A.STUDENT_ID), AVG(A.AVG), MIN(A.AVG), MAX(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE = {} GROUP BY S.SECTION ORDER BY S.SECTION".format(grade)
    cursor.execute(query)
    records = cursor.fetchall()

    if records is None or records==[]:
                print('No records found corresponding to entered credentials')
                return 0
            
    table_headers = [ 'GRADE','SECTION', 'NO. OF STUDENTS', 'CLASS AVERAGE', 'CLASS MINIMUM', 'CLASS MAXIMUM' ]
    print(tabulate( records, headers = table_headers, tablefmt='grid'))
    print()


def report_specific_section():
    grade = int(input('enter grade: '))
    section = input("enter section: ")

    query = "SELECT NAME, S.STUDENT_ID, A.SUB1, A.SUB2, A.SUB3, A.SUB4, A.SUB5, A.AVG, A.REMARKS FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE GRADE={} AND SECTION='{}' ORDER BY NAME".format(grade, section)
    cursor.execute(query)
    records = cursor.fetchall()

    if records is None or records == []:
                print('No records found corresponding to entered credentials')
                return 0
    
    query = "SELECT STREAM FROM STUDENT WHERE GRADE = {} AND SECTION = '{}'".format(grade, section)
    cursor.execute(query)
    stream_code = cursor.fetchone()[0]
    print(stream_code)
    sub1, sub2, sub3, sub4, sub5 = stream(stream_code)
    print(subq1, sub2, sub3, sub4, sub5, stream(stream_code))
    
    table_headers = [ 'NAME', 'STUDENT_ID', sub1, sub2, sub3, sub4, sub5, 'AVERAGE', 'REMARK']
    print(tabulate( records, headers = table_headers,  tablefmt = 'grid') )

    query = "SELECT COUNT(S.STUDENT_ID), MIN(A.AVG) , MAX(A.AVG), AVG(A.AVG)  FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE GRADE={}, SECTION='{}'".format(grade, section)
    cursor.execute(query)
    records = cursor.fetchall()
    if records is None or records==[]:
                print('No records found corresponding to entered credentials')
                return 0
            
    table_headers = ['NO. OF STUDENTS', 'CLASS MINIMUM', 'CLASS MAXIMUM', 'CLASS AVERAGE' ]
    print(tabulate(records, headers=table_headers, tablefmt = 'grid'))
    print()
def report_group_by_stream():
    grade = int(input('Enter grade: '))
    query = "SELECT S.STREAM, COUNT(A.STUDENT_ID), MIN(A.AVG), MAX(A.AVG), AVG(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE={} GROUP BY S.STREAM ORDER BY S.STREAM".format(grade)
    cursor.execute(query)
    records = cursor.fetchall()
    
    if records is None or records == []:
                print('No records found corresponding to entered credentials')
                return 0
    table_headers = ['STREAM_CODE', 'NO OF STUDENTS', 'STREAM MINIMUM', 'STREAM MAXIMUM', 'STREAM AVERAGE' ]
    print(tabulate(records, headers=table_headers, tablefmt='grid'))
    print()
def report_specific_stream():
for stream_code in streams:
    print(stream_code, streams[stream_code])
    print()
    stream_code = input('enter stream code: ')
    if stream_code not in streams:
        print('Invalid stream code')
        return 0
    i=1        
    for subject in streams[stream_code]:
        sub = 'SUB'+str(i)
        query = "SELECT MIN(A.{}), MAX(A.{}), AVG(A.{}) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.STREAM ='{}'".format(sub, sub, sub, stream_code)  
        cursor.execute(query)
        record = cursor.fetchone()
        if record is None or record[0] is None:
                print('No records found corresponding to entered credentials')
                return 0
        table_headers = ['MINIMUM', 'MAXIMUM', 'AVERAGE']
        print(subject)
        print(tabulate([record], headers=table_headers, tablefmt='grid'))
        print()
        i+=1
        
    query = "SELECT  COUNT(S.STUDENT_ID), AVG(A.AVG), MIN(A.AVG), MAX(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.STREAM='{}'".format(stream_code)
    cursor.execute(query)
    record = cursor.fetchone()
    if record is None or record[0] is None:
                print('No records found corresponding to entered credentials')
                return 0
            
    print(tabulate([record], headers=['NO. OF STUDENTS', 'STREAM AVERAGE', 'STREAM MIN', 'STREAM_MAX'], tablefmt = 'grid'))   
    print()
    
def report():

    print('\n', 'REPORT MENU', '\n')
    print("1. group by section")
    print("2. specific section")
    print("3. group by stream")
    print("4. specific stream")
    opt = int(input("enter option: "))

    if opt == 1:
        report_group_by_section()    

    elif opt == 2:
        report_specific_section()
        
    elif opt == 3:
        report_group_by_stream()
    elif opt == 4:
        report_specific_stream()


