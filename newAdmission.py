def newAdm():

    #user input values
    cpr = int(input('enter cpr number: '))
    name = input('enter name: ').strip()
    dob = input('enter dob YYYY-MM-DD: ').strip()
    stream = input('enter stream (sci, com, hum): ').strip
    clss = int(input('enter class (11-12): '))
    secn = input('enter section (A-Z): ').strip()
    tel = int(input('enter telephone number: '))
    pname = input('enter parent\'s name (each seperated by \' & \': ').partition(' & ')
    
    address = {'flat':0, 'bldg':0, 'road':0, 'block':0, 'area':0}
    print('enter address;')
    for k in address:
        address[k] = int(input('enter {}: '.format(k)))

    #to generate new grno by finding the maximum existing
    cmd = "SELECT MAX(GRNO) FROM STUDENT"
    cursor.execute(cmd) 
    maxgr = cursor.fetchone()
    gr = maxgr +1 

    #to insert
    cmd = "INSERT INTO STUDENT VALUES()"
    



