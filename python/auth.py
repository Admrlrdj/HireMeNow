session_data = []

def login():
    email_input = input("Email: ")
    password = input("Password: ")
    print("=====================================================")
    
    #* Buat variable baru untuk menyimpan pesan login dan role
    login_message, role = verify_login(email_input, password)

    if "Invalid" not in login_message:
        print(login_message)
        return role
    else:
        print("Login failed! Returning to main menu.\n")
        return None

def verify_login(email_input, password):
    #* Buat variable baru untuk menyimpan data session (diperlukan sekali untuk sisi perusahaan/company)
    global session_data
    
    #* Open database users.txt dengan mode baca/read sebagai variable file
    with open('database/users.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            
            if len(data) >= 6 and data[2].strip() == email_input and data[3].strip() == password:
                role = data[5].strip()
                name = data[1]
                email = data[2].strip()

                #* Buat variable baru untuk menyimpan data session
                session_data.append({"name": name, "email": email, "role": role})

                if role == 'admin':
                    return f"Welcome, {name}!", 'admin'
                elif role == 'user':
                    return f"Welcome, {name}!", 'user'
                elif role == 'company':
                    return f"Welcome, {name}!", 'company'

    return "Invalid email or password!", None

def register():
    print("=============== Register a New Account ===============")
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
    
    #* Open database users.txt dengan mode tambah/append sebagai variable file
    with open('database/users.txt', 'a') as file:
        file.write(f"{len(open('database/users.txt').readlines())+1}, {first_name} {last_name}, {email}, {password}, {telp}, {role}\n")
    
    print("\nRegistration successful! You can now log in.")
    return True
