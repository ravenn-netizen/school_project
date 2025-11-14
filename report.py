
#probs with report_specific_section function
#finished testing

import mysql.connector as sql
db = sql.connect(host='localhost', user='root', passwd='****', database='school')
cursor = db.cursor()

from tabulate import tabulate

streams={'H01':('English','Home Science','Psychology','Marketing','Sociology'), 'C01':('English','Accountancy','Business Studies','Economics','Mathematics'),'C02':('English','Accountancy','Business Studies','Economics','Informatics Practices'),'C03':('English','Accountancy','Business Studies','Economics','Marketing'),'S01':( 'English','Physics','Chemistry','Mathematics','Biology'),'S02':('English','Physics','Chemistry','Mathematics','Computer Science'),'S03':('English','Physics','Chemistry','Mathematics','Engineering Graphics'),'S04':('English','Physics','Chemistry','Biology','Computer Science'),'S05':('English','Physics','Chemistry','Biology','Bio-Technology'),'S06':('English','Physics','Chemistry','Mathematics','Artificial Intelligence')}
    
def report_group_by_section():
    grade = int(input('enter grade: '))
    term = input("enter term ('first', 'second' or 'third'): ").lower()
    query = "SELECT S.GRADE, S.SECTION, COUNT(A.STUDENT_ID), AVG(A.AVG), MIN(A.AVG), MAX(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE = {} AND A.TERM= '{}' GROUP BY S.SECTION ORDER BY S.SECTION".format(grade, term)
    cursor.execute(query)
    records = cursor.fetchall()

    if not records: #if no records found this statement is true and escapes the function
                print('No records found corresponding to entered grade')
                return 0
            
    table_headers = ['Grade','Section', 'No. of students', 'Class average', 'Class minimum', 'Class maximum']
    print(tabulate(records, headers =table_headers, tablefmt="psql"))


def report_specific_section():
    grade = int(input('enter grade: '))
    section = input("enter section: ").upper()
    term = input("enter term ('first', 'second' or 'third'): ").lower()
    query = "SELECT NAME, S.STUDENT_ID, A.SUB1, A.SUB2, A.SUB3, A.SUB4, A.SUB5, A.AVG, A.REMARKS FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE={} AND S.SECTION='{}' AND A.TERM ='{}' ORDER BY S.NAME".format(grade, section, term)
    cursor.execute(query)
    records = cursor.fetchall()

    if not records: #''
                print('No records found corresponding to entered grade and/or section')
                return 0
    
    query = "SELECT STREAM FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE = {} AND S.SECTION = '{}' AND A.TERM='{}'".format(grade, section, term)
    cursor.execute(query)
    stream_code = cursor.fetchone()[0]
    sub1, sub2, sub3, sub4, sub5 = streams[stream_code]

    
    table_headers =['NAME', 'STUDENT_ID', sub1, sub2, sub3, sub4, sub5, 'AVERAGE', 'REMARK']
    print(tabulate(records, headers=table_headers, tablefmt = 'grid'))
    print()
    
    query = "SELECT COUNT(S.STUDENT_ID), MIN(A.AVG) , MAX(A.AVG), AVG(A.AVG)  FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE={} AND S.SECTION='{}' AND A.TERM='{}' ".format(grade, section, term)
    cursor.execute(query)
    rec= cursor.fetchone()
    if not rec: 
                print('No records found corresponding to entered credentials')
                return 0
            
    print('Number of students enrolled:', rec[0])
    print('Class average score:', rec[1])
    print('Class minimum score:', rec[2])
    print('Class maximum score:', rec[3])
    print()
    
def report_group_by_stream():
    grade = int(input('Enter grade: '))
    term = input("enter term ('first', 'second' or 'third'): ").lower()
    query = "SELECT S.STREAM, COUNT(A.STUDENT_ID), MIN(A.AVG), MAX(A.AVG), AVG(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.GRADE={} AND A.TERM = '{}' GROUP BY S.STREAM ORDER BY S.STREAM".format(grade, term)
    cursor.execute(query)
    recs = cursor.fetchall()
    
    if not recs:
                print('No records found corresponding to entered credentials')
                return 0
    for rec in recs:
        print('Stream:', rec[0])
        print('Number of students enrolled:', rec[1])
        print('Minimum score:', rec[2])
        print('Maximum score:', rec[3])
        print('Average score:', rec[4])
        print()
    
def report_specific_stream():
    grade = int(input('enter grade (11/12): '))
    term = input("enter term ('first', 'second' or 'third'): ").lower()
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
        query = "SELECT MIN(A.{}), MAX(A.{}), AVG(A.{}) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.STREAM ='{}' AND A.TERM='{}' AND S.GRADE={}".format(sub, sub, sub, stream_code, term, grade)  
        cursor.execute(query)
        rec = cursor.fetchone()
        if not rec:
                print('No records found corresponding to entered credentials')
                return 0
        print(subject)
        print('Minimum score:', rec[0])
        print('Maximum score:', rec[1])
        print('Average score:', rec[2])
        print()
        i+=1
            
    query = "SELECT  COUNT(S.STUDENT_ID), AVG(A.AVG), MIN(A.AVG), MAX(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE S.STREAM='{}'  AND A.TERM ='{}' AND GRADE={}".format(stream_code, term, grade)
    cursor.execute(query)
    rec = cursor.fetchone()
    if not rec:
        print('No records found corresponding to entered credentials')
        return 0
                
    print('Number of students enrolled:', rec[0])
    print('Minimum score:', rec[1])
    print('Maximum score:', rec[2])
    print('Average score:', rec[3])
    print()
    
def report():
    while True:
        print('\n', 'REPORT MENU', '\n')
        print("1. group by section")
        print("2. specific section")
        print("3. group by stream")
        print("4. specific stream")
        print("5. exit\n")
        opt = int(input("enter option: "))

        if opt == 1:
            report_group_by_section()    
        elif opt == 2:
            report_specific_section()
        elif opt == 3:
            report_group_by_stream()
        elif opt == 4:
            report_specific_stream()
        elif opt ==5:
            return 0
report()

