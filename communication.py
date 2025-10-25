def createTableAnnouncements():
    cmd = "CREATE TABLE ANNOUNCEMENT(REF INT, FROM varchar(20), TO_TYPE varchar(20), TO varchar(20), DATE date, CONTENT text)"
    cursor.execute(cmd)

def sendAnnouncement():
    sender = userid
    print('choose reciever type')
    print('1. grade')
    print('2. class')
    print('3. student')
    opt = int(input('enter option: '))
    if opt==1:
        to_type = 'grade'
        receipient = input('enter grade: ')
    elif opt==2:
        to_type  = 'class'
        receipient = input('enter class: ')

    elif opt==3:
        to_type = 'student'
        receipient = input('enter id: ')
    
    cmd = "SELECT MAX(REF) FROM ANNOUNCEMENT"
    cursor.execute(cmd)
    ref = cursor.fetchone() + 1


    date = input('enter date YYYY-MM-DD: ')
    subject = input('enter subject: ')
    content = input('enter content: ')
    file = open("message{}", "w").format(ref)
    file.write(date + '\n')
    file.write(subject + '\n')
    file.write(content + '\n')
    file.close()

    
    #to add into to file 
    cmd = "INSERT INTO ANNOUNCEMENT VALUES(ref, userid, to_type, receipient, date, file)"
    cursor.execute(cmd)
    db.commit()
