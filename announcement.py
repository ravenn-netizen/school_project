#UNDER TESTING!!
#PLEASE DONT RUN IT JUST YET

def createTableAnnouncement():
    cmd = "USE SCHOOL"
    cursor.execute(cmd)
    cmd = "CREATE TABLE ANNOUNCEMENT(REF INT, SENDER INT, RECEIPIENT_TYPE varchar(20), RECEIPIENT varchar(20), DATE date, SUBJECT text, CONTENT text)" #here text is a datatype which is basically a string with no length constraint
    cursor.execute(cmd)

cursor.execute('USE SCHOOL')
def send_announcement():
    
    sender = user_id

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
    
    if result is None or result[0] is None:
        ref = 1
    else:
        ref = result[0] + 1

    #to input anncuncement content
    date = input('enter date YYYY-MM-DD: ')
    subject = input('enter subject: ')
    content = input('enter content: ')
    
    #to add into to file 
    cmd = "INSERT INTO ANNOUNCEMENT VALUES({}, '{}', {}, '{}', '{}','{}', '{}')".format(ref, sender, receipient_type, receipient, date, subject, content)
    cursor.execute(cmd)

    db.commit()

def received_announcement():
    
    #to check for announcements for user and add to their inbox 
    cmd = "SELECT GRADE, SECTION FROM STUDENT"
    cursor.execute(cmd)
    grade, section = cursor.fetchall()[0]
    
    cmd = "SELECT * FROM ANNOUNCEMENT"
    cursor.execute(cmd)
    records = cursor.fetchall()

    if records is None or records[0] is None:
        print('No announcements in inbox')
        print('Check another time :)')
        return 0

    inbox=[]
    for i in range(len(records)):
        record = records[i]
        receipient_type = record[2]
        receipient = record[3]
        if receipient_type == 'grade' and receipient == grade:
            inbox.append(record)

        elif receipient_type == 'section':
            receipient = receipient.split('&')

            if receipient[0].strip() == grade and receipient[1].strip() == section:
                inbox.append(record)

        elif receipient_type == 'student':
            if int(receipient) == user_id:
                inbox.append(record)
            
    #to open each message
    print('announcements in inbox:', len(inbox))

    if len(inbox) > 0:
        for i in range(len(inbox)):
            record = inbox[i]
            i+=1
            print(str(i)+'.', record[-2])  #here record[-2] is the subject of the announcement

            while true:

                print('\nEnter 0 for option to exit')
                opt = int(input('enter message to open: '))
                if opt == 0:
                    return 0                
                elif opt > len(inbox):  #to check if entered optionis within range; if not loops over
                    print('enter valid option')
                    continue 

                message = inbox[opt-1]


                
                #to find sending staff's name as only their staff_id is stored in the table    
                cmd = "SELECT NAME FROM STAFF WHERE STAFF_ID = '{}'".format(message[1])
                cursor.execute(cmd)
                sender_name = cursor.fetchone()[0]
                print('FROM:', sender_name, '\n')
                print('SUBJECT:', message[-2], '\n')
                print('CONTENT:', '\n', message[-1], '\n')

    else:
        print('No announcement in inbox')
        print('Check another time :)')

