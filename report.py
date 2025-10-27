def report():

    print('\n', 'REPORT MENU', '\n')
    print("1. group by class")
    print("2. specific class")
    opt = int(input("enter option: "))
       
        
    if opt == 1:

        query = "SELECT S.GRADE, S.SECTION, COUNT(A.STUDENT_ID), avg(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A GROUP BY GRADE, SECTION ORDER BY GRADE, SECTION".format(grade, section)
        cursor.execute(query)
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
