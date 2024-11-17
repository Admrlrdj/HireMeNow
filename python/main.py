from auth import login, register
import admin
import user
import company

def main_menu():
    while True:
        print("=============== Welcome to HireMeNow ===============")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            role = login()
            if role:
                print(f"You are logged in as {role}.")
                
                if role == 'admin':
                    admin.admin()
                elif role == 'user':
                    user.user()
                elif role == 'company':
                    company.company()
                break
        elif choice == '2':
            registration_status = register()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
