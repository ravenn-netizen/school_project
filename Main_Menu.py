def Main_Menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Staff (Teacher) Sign Up")
        print("2. Staff (Teacher) Sign In")
        print("3. Student Sign In")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            staff_sign_up()  # defined in sign_up&sign_in.py
        elif choice == '2':
            if staff_sign_in():
                teacher_menu()
            else:
                print("Invalid staff credentials. Try again.")
        elif choice == '3':
            if student_sign_in():  ]
                student_menu()
            else:
                print("Invalid student credentials. Try again.")
        elif choice == '4':
            print("Exiting program!")
            break
        else:
            print("Invalid choice, please enter 1, 2, 3, or 4.")


