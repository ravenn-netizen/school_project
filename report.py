def report():

    print('\n', 'REPORT MENU', '\n')
    print("1. group by class")
    print("2. specific class")
    opt = int(input("enter option: "))
       
        
    if opt == 1:

        query = "SELECT S.GRADE, S.SECTION, COUNT(A.STUDENT_ID), avg(A.AVG) FROM STUDENT S NATURAL JOIN ACADEMIC A GROUP BY GRADE, SECTION".format(grade, section)
        cursor.execute(query)
        records = cursor.fetchall()
        for i in records:
            for k in i:
                print(k, end='\t')
            print()

    elif opt == 2:

        grade = int(input('enter grade: '))
        section = input("enter section: ")

        query = "SELECT NAME, STUDENT.STUDENT_ID, SUB1, SUB2, SUB3, SUB4, SUB5, AVG, REMARK FROM STUDENT NATURAL JOIN ACADEMIC WHERE GRADE={} AND SECTION={}".format(grade, section)
        cursor.execute(query)
        records = cursor.fetchall()
        for i in records:
            for k in i:
                print(k, end='\t')
            print()

        query = "SELECT COUNT(S.STUDENT_ID), MIN(A.AVG), MAX(A.AVG), AVG(A.AVERAGE) FROM STUDENT S NATURAL JOIN ACADEMIC A "
