import json

def user(role_input):
    user_list = []
    with open('database/users.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            
            if data[5].strip() == role_input:
                if role_input == 'admin' or role_input == 'user':
                    user_info = {
                        'user_no': data[0],
                        'name': data[1].strip(),
                        'email': data[2].strip(),
                        'password': data[3].strip(),
                        'telp': data[4].strip(),
                        'role': data[5].strip()
                    }
                elif role_input == 'company':
                    user_info = {
                        'user_no': data[0],
                        'company_name': data[1].strip(),
                        'email': data[2].strip(),
                        'password': data[3].strip(),
                        'telp': data[4].strip(),
                        'role': data[5].strip()
                    }
                user_list.append(user_info)
    
    return user_list

role_input = input("Enter role to filter (admin/user/company): ").strip().lower()

if role_input in ['admin', 'user', 'company']:
    users = user(role_input)
    users_json = json.dumps(users, indent=4)
    print(users_json)
else:
    print("Invalid role! Please enter either 'admin', 'user', or 'company'.")

# def search_user_by_name_partial(user_input):
#     user_list = []
#     with open('database/users.txt', 'r') as file:
#         for line in file:
#             data = line.strip().split(',')
            
#             if user_input.lower() in data[1].strip().lower():
#                 user_info = {
#                     'user_no': data[0],
#                         'name': data[1].strip(),
#                         'email': data[2].strip(),
#                         'password': data[3].strip(),
#                         'telp': data[4].strip(),
#                         'role': data[5].strip()
#                 }
#                 user_list.append(user_info)

#     return user_list

# user_input = input("Enter a keyword for company name to search: ").strip().lower()

# users = search_user_by_name_partial(user_input)
# if users:
#     users_json = json.dumps(users, indent=4)
#     print(users_json)
# else:
#     print(f"No users found for companies containing '{user_input}'.")
