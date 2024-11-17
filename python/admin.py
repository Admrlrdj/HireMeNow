def admin():
    while True:
        print("=============== Admin Menu ===============")
        print("1. Add User")
        print("2. View User")
        print("3. Edit User")
        print("4. Remove User")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            read_user()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_user():
    print("=============== Add User ===============")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    telp = input("Telp: ")
    
    with open('database/users.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if email == data[2].strip():
                print("Email already exists! Please try registering with a different email.")
                return False
    
    while True:
        role = input("Enter role (user/company): ").strip().lower()
        if role in ['user', 'company']:
            break
        print("Invalid role! Please enter either 'user' or 'company'.")
    
    with open('database/users.txt', 'a') as file:
        file.write(f"{len(open('database/users.txt').readlines())+1}, {first_name} {last_name}, {email}, {password}, {telp}, {role}\n")

    print("\nCreate User successful!")
    return True

def read_user():
    print("=============== View User ===============")

    users = []
    with open('database/users.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            user_info = {
                'user_no': data[0],
                'name': data[1].strip(),
                'email': data[2].strip(),
                'password': data[3].strip(),
                'telp': data[4].strip(),
                'role': data[5].strip()
            }
            users.append(user_info)

    sort_order = input("Sort by name (ascending/descending): ").strip().lower()
    
    if sort_order == "ascending":
        users = sorted(users, key=lambda x: x['name'])
    elif sort_order == "descending":
        users = sorted(users, key=lambda x: x['name'], reverse=True)
    else:
        print("Invalid sorting option! Defaulting to ascending order.")
        users = sorted(users, key=lambda x: x['name'])

    for user in users:
        print(f"User No     : {user['user_no']}")
        print(f"Name        : {user['name']}")
        print(f"Email       : {user['email']}")
        print(f"Password    : {user['password']}")
        print(f"Telp        : {user['telp']}")
        print(f"Role        : {user['role']}")
        print("------------------------------")

    search_choice = input("Do you want to search for a user? (yes/no): ").strip().lower()
    
    if search_choice == 'yes':
        search_term = input("Enter name or email to search: ").strip().lower()
        found_users = [user for user in users if search_term in user['name'].lower() or search_term in user['email'].lower()]
        
        if found_users:
            for user in found_users:
                print(f"User No     : {user['user_no']}")
                print(f"Name        : {user['name']}")
                print(f"Email       : {user['email']}")
                print(f"Password    : {user['password']}")
                print(f"Telp        : {user['telp']}")
                print(f"Role        : {user['role']}")
                print("------------------------------")
        else:
            print("No user found with the given search term.")
    
    return True

def update_user():
    print("=============== Update User ===============")
    
    users = []
    with open('database/users.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            user_info = {
                'user_no': data[0],
                'name': data[1].strip(),
                'email': data[2].strip(),
                'password': data[3].strip(),
                'telp': data[4].strip(),
                'role': data[5].strip()
            }
            users.append(user_info)

    for user in users:
        print(f"User No     : {user['user_no']}")
        print(f"Name        : {user['name']}")
        print(f"Email       : {user['email']}")
        print(f"Password    : {user['password']}")
        print(f"Telp        : {user['telp']}")
        print(f"Role        : {user['role']}")
        print("------------------------------")
    
    user_no = input("Enter User No to update: ").strip()
    
    user_found = False
    for user in users:
        if user['user_no'] == user_no:
            user_found = True
            print("Updating User Information:")
            user['name'] = input(f"New Name (current: {user['name']}): ") or user['name']
            user['email'] = input(f"New Email (current: {user['email']}): ") or user['email']
            user['password'] = input(f"New Password (current: {user['password']}): ") or user['password']
            user['telp'] = input(f"New Telp (current: {user['telp']}): ") or user['telp']
            user['role'] = input(f"New Role (current: {user['role']}): ") or user['role']
            print("User information updated successfully.")
            break
    
    if not user_found:
        print("User No not found. No updates made.")
        return False
    
    with open('database/users.txt', 'w') as file:
        for user in users:
            file.write(f"{user['user_no']}, {user['name']}, {user['email']}, {user['password']}, {user['telp']}, {user['role']}\n")
    
    print("All updates saved successfully.")
    return True

def delete_user():
    print("=============== Delete User ===============")
    
    users = []
    with open('database/users.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            user_info = {
                'user_no': data[0],
                'name': data[1].strip(),
                'email': data[2].strip(),
                'password': data[3].strip(),
                'telp': data[4].strip(),
                'role': data[5].strip()
            }
            users.append(user_info)

    for user in users:
        print(f"User No     : {user['user_no']}")
        print(f"Name        : {user['name']}")
        print(f"Email       : {user['email']}")
        print(f"Password    : {user['password']}")
        print(f"Telp        : {user['telp']}")
        print(f"Role        : {user['role']}")
        print("------------------------------")
    
    user_no = input("Enter User No to delete: ").strip()
    
    user_found = False
    for user in users:
        if user['user_no'] == user_no:
            user_found = True
            print("User Information:")
            print(f"User No     : {user['user_no']}")
            print(f"Name        : {user['name']}")
            print(f"Email       : {user['email']}")
            print(f"Password    : {user['password']}")
            print(f"Telp        : {user['telp']}")
            print(f"Role        : {user['role']}")
            print("------------------------------")
            confirmation = input("Are you sure you want to delete this user? (yes/no): ").strip().lower()
            if confirmation == "yes":
                users.remove(user)
                print("User deleted successfully.")
                break
            else:
                print("Deletion canceled.")
                return False
    
    if not user_found:
        print("User No not found. No deletion made.")
        return False
    
    with open('database/users.txt', 'w') as file:
        for user in users:
            file.write(f"{user['user_no']}, {user['name']}, {user['email']}, {user['password']}, {user['telp']}, {user['role']}\n")
    
    return True