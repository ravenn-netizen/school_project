from tabulate import tabulate
import mysql.connector as sql

db = sql.connect(host='localhost', user='root', passwd='****', database='SCHOOL')
cursor = db.cursor()


streams = {
    'H01': ('English', 'Home Science', 'Psychology', 'Marketing', 'Sociology'),
    'C01': ('English', 'Accountancy', 'Business Studies', 'Economics', 'Mathematics'),
    'C02': ('English', 'Accountancy', 'Business Studies', 'Economics', 'Informatics Practices'),
    'C03': ('English', 'Accountancy', 'Business Studies', 'Economics', 'Marketing'),
    'S01': ('English', 'Physics', 'Chemistry', 'Mathematics', 'Biology'),
    'S02': ('English', 'Physics', 'Chemistry', 'Mathematics', 'Computer Science'),
    'S03': ('English', 'Physics', 'Chemistry', 'Mathematics', 'Engineering Graphics'),
    'S04': ('English', 'Physics', 'Chemistry', 'Biology', 'Computer Science'),
    'S05': ('English', 'Physics', 'Chemistry', 'Biology', 'Bio-Technology'),
    'S06': ('English', 'Physics', 'Chemistry', 'Mathematics', 'Artificial Intelligence')
}

# Authentication 
def admin_sign_in():
    while True:
        password = input("Enter admin password: ")
        if password == "admin's password":  # We need to make a passwd
            print("Admin signed in.")
            return True
        else:
            print("Incorrect password. Try again or enter 'exit' to return to menu.")
            if input("Continue? (yes/no): ").lower() != "yes":
                return False

def staff_sign_in():
    cursor.execute("SELECT STAFFID FROM STAFF")
    valid_ids = [id[0] for id in cursor.fetchall()]
    while True:
        try:
            staff_id = int(input("Enter staff ID: "))
            if staff_id in valid_ids:
                cursor.execute(f"SELECT PASSWORD FROM STAFF WHERE STAFFID={staff_id}")
                correct_password = cursor.fetchone()[0]
                entered_password = input("Enter password: ")
                if entered_password == correct_password:
                    print("Staff signed in.")
                    return staff_id
                else:
                    print("Wrong password, try again.")
            else:
                print("Staff ID not found.")
        except ValueError:
            print("Please enter a valid number.")

def student_sign_in():
    cursor.execute("SELECT STUDENT_ID FROM STUDENT")
    valid_ids = [id[0] for id in cursor.fetchall()]
    while True:
        try:
            student_id = int(input("Enter student ID: "))
            if student_id in valid_ids:
                cursor.execute(f"SELECT PASSWORD FROM STUDENT WHERE STUDENT_ID={student_id}")
                correct_password = cursor.fetchone()[0]
                entered_password = input("Enter password: ")
                if entered_password == correct_password:
                    print("Student signed in.")
                    return student_id
                else:
                    print("Wrong password, try again.")
            else:
                print("Student ID not found.")
        except ValueError:
            print("Please enter a valid number.")


