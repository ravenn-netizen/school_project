#not complete yet
#PLEASE DONT RUN THIS YET!!

def report():

    print('\n', 'REPORT MENU', '\n')
    print("1. group by section")
    print("2. specific section")
    print("3. group by stream")
    print("4. specific stream")
    opt = int(input("enter option: "))
       
        
    if opt == 1:
        grade = int(input('enter grade: ')
        query = "SELECT S.GRADE, S.SECTION, COUNT(A.STUDENT_ID), avg(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC WHERE GRADE = {} A GROUP BYSECTION ORDER BYSECTION".format(grade)
        records = cursor.fetchall()
        for i in records:
            for k in i:
                print(k, end='\t')
            print()

    elif opt == 2:

        grade = int(input('enter grade: '))
        section = input("enter section: ")

        query = "SELECT NAME, S.STUDENT_ID, A.SUB1, A.SUB2, A.SUB3, A.SUB4, A.SUB5, A.AVG, A.REMARK FROM STUDENT S NATURAL JOIN ACADEMIC A WHERE GRADE={} AND SECTION={} ORDER BY NAME".format(grade, section)
        cursor.execute(query)
        records = cursor.fetchall()
        for i in records:
            for k in i:
                print(k, end='\t')
            print()

        query = "SELECT COUNT(S.STUDENT_ID) AS TOTAL STUDENTS, MIN(A.AVG) AS MINIMUM_AVERAGE, MAX(A.AVG) AS MAXIMUM_AVERAGE, AVG(A.AVERAGE) AS CLASS_AVERAGE FROM STUDENT S NATURAL JOIN ACADEMIC A "
        cursor.execute(query)
        records = cursor.fetchall()
        for i in records:
            for k in i:
                print(k, end='\t')
            print()      
    elif opt == 3:
        query = "SELECT COUNT(A.STUDENT_ID) AS NO_OF_STUDENTS, MIN(A.AVERAGE) AS MINIMUM_AVERAGE, MAX(A.AVERAGE) AS MAXIMUM_AVERAGE, AVG(A.AVERAGE) AS STREAM_AVERAGE WHERE STUDENTS S NATURAL JOIN ACADEMICS A GROUP BY S.STREAM"
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            for k in record:
                print(k, end='\t')
            print()
    elif opt == 4:
        for stream_code, subjects in streams:
            print(stream_code, subjects)
        stream = input('enter stream code: ')
        query = "SELECT COUNT(A.STUDENT_ID) AS NO_OF_STUDENTS, MIN(A.AVERAGE) AS MINIMUM_AVERAGE, MAX(A.AVERAGE) AS MAXIMUM_AVERAGE, AVG(A.AVERAGE) AS STREAM_AVERAGE FROM STUDENTS S NATURAL JOIN ACADEMICS A GROUP BY S.STREAM WHERE S.STREAM={}".format(stream)
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            for k in record:
                print(k, end='\t')
            print()
        
