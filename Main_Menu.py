def Main_Menu():
    while True:
        print("\n--- School Management System ---")
        print("1. Staff Sign In")
        print("2. Student Sign In")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            staff_id = staff_sign_in()
            if staff_id != 0:
                staff_menu(staff_id)
        elif choice == '2':
            student_id = student_sign_in()
            if student_id != 0:
                student_menu(student_id)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def staff_menu(staff_id):
    while True:
        print("\n--- Staff Menu ---")
        print("1. Student Info")
        print("2. Send Announcement")
        print("3. Reports")
        print("4. Update Password")
        print("5. Logout")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            while True:
                print("\n--- Student Info ---")
                print("a. New Admission")
                print("b. Search Student")
                print("c. Marks Management")
                print("d. Update Student Info")
                print("e. Remove Student")
                print("f. Back to Staff Menu")
                sub_choice = input("Select option (a-f): ").lower()

                #functions based on sub_choice
                if sub_choice == 'a':
                    new_student()
                elif sub_choice == 'b':
                    search_student_menu()
                elif sub_choice == 'c':
                    marksmanagement()
                elif sub_choice == 'd':
                    update_student_info_menu()
                elif sub_choice == 'e':
                    del_student()
                elif sub_choice == 'f':
                    break
                else:
                    print("Invalid option, please try again.")
                    
        elif choice == '2':
            send_announcement()
        elif choice == '3':
            report()
        elif choice == '4':
            update_staff_pass()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice!")


def student_menu(student_id):
    while True:
        print("\n--- Student Menu ---")
        print("1. View Announcements")
        print("2. View Result")
        print("3. Update Password")
        print("4. Logout")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            received_announcement()
        elif choice == '2':
            progress_report()
        elif choice == '3':
            update_student_password()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice!")

main_menu()
