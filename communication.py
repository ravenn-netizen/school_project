def sendMessage():
    sender = cpr 
    while True:
        recipient_type = input('enter recipient type (student or staff): ').upper()
        recipient_name = input('to (name): ')
        
        query = "SELECT NAME FROM '{}'".format(recipient_type)
        cursor.execute(query)
        records = cursor.fetchall()
        if recipient_name in records:
            break 
        else: 
            print('entered recipient type or recipient name is incorrect')
            print('please try again')

    query = "SELECT CPR FROM '{}' WHERE NAME = '{}'".format(recipient_type, recipient_name)
    cursor.execute()
    recipient = cursor.fetchone()

    message = input('Your message:', end='\n')
    messageFile = open('temp', mode='w')
    messageFile.write(message)
    date = input('date (YYYY-MM-DD): ')

    query = "SELECT max(REF) FROM COMMUNICATION"
    cursor.execute(query)
    ref = cursor.fetchone() + 1

    cmd = "INSERT INTO COMMUNICATION VALUES({}, '{}', '{}', '{}', '{}', {}, '{}')".format(ref, sender, recipient, user_type, recipient_type, messageFile, date)
    cursor.execute(cmd)
    db.commit()
