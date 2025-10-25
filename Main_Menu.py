def main_menu():
   
    while True:
        print("\n=== SCHOOL PROJECT MAIN MENU ===")
        print("1. Add new student")
        print("2. View student details")
        print("3. Update student records")
        print("4. Delete student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1–5): "))

            if choice == 1:
                add_student()          
            elif choice == 2:
                view_student()
            elif choice == 3:
                update_student()
            elif choice == 4:
                delete_student()
            elif choice == 5:
                print("Exiting")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Enter a number only.")
