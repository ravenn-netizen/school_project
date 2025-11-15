def send_announcement(staff_id):
    sender = staff_id

    #to input receiver and their type
    print('choose receiver type')
    print('1. grade')
    print('2. section')
    print('3. student')
    opt = int(input('enter option: '))
    if opt==1:
        receipient_type = 'grade'
        receipient = input('enter grade: ')
    elif opt==2:
        receipient_type  = 'section'
        receipient = input('enter grade and section (grade&section): ')
    elif opt==3:
        receipient_type = 'student'
        receipient = input('enter id: ')

    # to create reference for announcement
    cmd = "SELECT MAX(REF) FROM ANNOUNCEMENT"
    cursor.execute(cmd)
    result = cursor.fetchone()
    
    if not result:
        ref = 1
    else:
        ref = result[0] + 1

    #to input announcement content
    date = input('enter date YYYY-MM-DD: ')
    subject = input('enter subject: ')
    content = input('enter content: ')
    
    #to add into to file 
    cmd = "INSERT INTO ANNOUNCEMENT VALUES({}, {}, '{}', '{}', '{}','{}', '{}')".format(ref, sender, receipient_type, receipient, date, subject, content)
    cursor.execute(cmd)

    db.commit()

def received_announcement(student_id):

    #to check for announcements for user and add to their inbox 
    cmd = "SELECT GRADE, SECTION FROM STUDENT WHERE STUDENT_ID={}".format(student_id)
    cursor.execute(cmd)
    grade, section = cursor.fetchone()
    
    cmd = "SELECT * FROM ANNOUNCEMENT"
    cursor.execute(cmd)
    records = cursor.fetchall()

    if not records :
        print('No announcements in inbox')
        print('Check another time :)\n')
        return 0

    inbox=[]
    for record in records:

        receipient_type = record[2]
        receipient = record[3]
        if receipient_type == 'grade' and int(receipient) == grade:
            inbox.append(record)

        elif receipient_type == 'section':
            receipient = receipient.split('&')

            if int(receipient[0])== grade and receipient[1] == section:
                inbox.append(record)

        elif receipient_type == 'student':
            if int(receipient) == student_id:
                inbox.append(record)

    #to open each message
    print('announcements in inbox:', len(inbox))
    if not inbox:
        print('No announcement in inbox')
        print('Check another time :)\n')
        return 0

    if len(inbox):
        i=0
        for record in records:
            i+=1
            print(str(i)+'.', record[-2])  #here record[-2] is the subject of the announcement

            while True:

                print('\nEnter 0 for option to exit')
                opt = int(input('enter message to open: '))
                if opt == 0:
                    return 0                
                elif opt > len(inbox) :  #to check if entered optionis within range; if not loops over
                    print('enter valid option')
                    continue 

                message = inbox[opt-1]
                
                #to find sending staff's name as only their staff_id is stored in the table    
                cmd = "SELECT NAME FROM STAFF WHERE STAFF_ID = {}".format(message[1])
                cursor.execute(cmd)
                sender_name = cursor.fetchone()[0]
                print('FROM:', sender_name, '\n')
                print('SUBJECT:', message[-2], '\n')
                print('CONTENT:', '\n', message[-1], '\n')

    else:
        print('No announcement in inbox')
        print('Check another time :)')
