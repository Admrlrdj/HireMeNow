from auth import session_data

def company():
    while True:
        print("=============== Company Menu ===============")
        print("1. Add Joblist")
        print("2. View Joblist")
        print("3. Edit Joblist")
        print("4. Remove Joblist")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_joblist()
        elif choice == '2':
            read_joblist()
        elif choice == '3':
            update_joblist()
        elif choice == '4':
            delete_joblist()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_joblist():
    if not session_data:
        print("You need to log in first!")
        return False
    
    hrd_name = session_data[0]["name"]
    hrd_email = session_data[0]["email"]
    
    print("=============== Add Joblist ===============")
    
    company_name = input("Company Name: ")
    job_type = input("Job Type: ")
    instagram = input("Instagram: ")

    with open('database/job.txt', 'a') as file:
        file.write(f"{len(open('database/job.txt').readlines())+1}, {company_name}, {hrd_email}, {job_type}, {instagram}, {hrd_name}\n")
    
    print("\nJob listing added successfully!")
    return True

def read_joblist():
    if not session_data:
        print("You need to log in first!")
        return False

    hrd_email = session_data[0]["email"]
    
    print("=============== View Joblist ===============")
    with open('database/job.txt', 'r') as file:
        found = False
        for line in file:
            data = line.strip().split(', ')
            job_hrd_email = data[2]

            if job_hrd_email == hrd_email:
                print(line.strip())
                found = True
        
        if not found:
            print("No job listings found for your company.")

    return True

def update_joblist():
    if not session_data:
        print("You need to log in first!")
        return False

    hrd_email = session_data[0]["email"]
    hrd_name = session_data[0]["name"]
    
    job_no = input("Enter the job number to edit: ")
    
    with open('database/job.txt', 'r') as file:
        lines = file.readlines()
    
    updated = False
    
    with open('database/job.txt', 'w') as file:
        for line in lines:
            data = line.strip().split(', ')
            job_no_in_file = data[0]
            company_name_in_file = data[1]
            hrd_email_in_file = data[2]
            
            if job_no_in_file == job_no and hrd_email_in_file == hrd_email:
                new_job_type = input("Enter the new job type: ")    
                new_instagram = input("Enter the new instagram: ")
                
                line = f"{job_no}, {company_name_in_file}, {hrd_email_in_file}, {new_job_type}, {new_instagram}, {hrd_name}\n"
                updated = True

            file.write(line)
    
    if updated:
        print("\nJob listing updated successfully!")
    else:
        print("\nJob listing not found or you are not authorized to edit this listing.")
    return True


def delete_joblist():    
    print("=============== Remove Joblist ===============")
    job_no = input("Enter the job number to remove: ")
    with open('database/job.txt', 'r') as file:
        lines = file.readlines()
    with open('database/job.txt', 'w') as file:
        for line in lines:
            data = line.strip().split(', ')
            if data[0] == job_no:
                continue
            file.write(line)

    print("\nJob listing removed successfully!")
    return True