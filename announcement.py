def createTableAnnouncements():
    cmd = "CREATE TABLE ANNOUNCEMENT(REF INT, SENDER varchar(20), RECEIPIENT_TYPE varchar(20), RECEIPIENT varchar(20), DATE date, CONTENT text)"
    cursor.execute(cmd)

def send_announcement():
    sender = userid

    #to input receiver and their type
    print('choose receiver type')
    print('1. grade')
    print('2. class')
    print('3. student')
    opt = int(input('enter option: '))
    if opt==1:
        receipient_type = 'grade'
        receipient = input('enter grade: ')
    elif opt==2:
        receipient_type  = 'class'
        receipient = input('enter class (grade & section): ')
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

    filename = "message" + str(ref)
    with open(filename, "w") as file:
        file.write("subject: " + subject + '\n')
        file.write("date: "+ date + '\n')
        file.write(content)
    
    
    #to add into to file 
    cmd = "INSERT INTO ANNOUNCEMENT VALUES({}, '{}', '{}', '{}', '{}', '{}')".format(ref, userid, receipient_type, receipient, date, filename)
    cursor.execute(cmd)

   
    db.commit()

def received_announcement():
    
    #to check for announcements for user and add to their inbox 
    cmd = "SELECT CLASS, SECTION FROM STUDENT"
    cursor.execute(cmd)
    grade, section = cursor.fetchall()
    
    cmd = "SELECT * FROM ANNOUNCEMENT"
    cursor.execute(cmd)
    records = cursor.fetchall()

    inbox=[]
    for _ in range(len(records)):
        record = records[i]
        receipient_type = record[2]
        receipient = record[3]
        if receipient_type == 'grade' and receipient == grade:
            inbox.append(record)

        elif receipient_type == 'class':
            receipient.partition('&')

            if receipient[0].strip() == grade and receipient[1].strip() == section:
                inbox.append(record)

        elif receipient_type == 'student':
            if receipient == user_id:
                inbox.append(record)
            
    #to open each message
    print('announcements in inbox: ', len(inbox))
    if len(inbox)>0:
    
        for i in range(len(inbox)):
            record = inbox[i]
            message = open(record[-1], 'r')
            subject = readline(message)
            print(i+1, '. ', subject)

        while True:
            opt = int(input('enter message to open: '))
            message = inbox[opt-1]
            print('subject: ', readline(message), end='\n\n')
            print(read(message), end='\n\n')

            opt = input('open another message? (y/n): ').strip().lower()
            if opt == 'n':
                break
    
    else:
        print('no announcements in inbox')
