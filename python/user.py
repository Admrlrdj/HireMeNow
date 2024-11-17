def user():
    while True:
        print("=============== User Menu ===============")
        print("1. View Job List")
        print("2. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            read_joblist()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def read_joblist():
    print("=============== View Joblist ===============")
    
    with open('database/job.txt', 'r') as file:
        lines = file.readlines()
    
    if not lines:
        print("No job listings available.")
        return False
    
    page_size = 5
    total_pages = (len(lines) // page_size) + (1 if len(lines) % page_size != 0 else 0)
    
    page_num = 1
    while True:
        start_idx = (page_num - 1) * page_size
        end_idx = min(start_idx + page_size, len(lines))
        
        print(f"Page {page_num}/{total_pages}")
        for i in range(start_idx, end_idx):
            line = lines[i].strip()
            data = line.split(', ')
            job_no, company_name, hrd_email, job_type, instagram, hrd_name = data

            print(f"Job No      : {job_no}")
            print(f"Company     : {company_name}")
            print(f"HRD Email   : {hrd_email}")
            print(f"Job Type    : {job_type}")
            print(f"Instagram   : {instagram}")
            print(f"HRD Name    : {hrd_name}")
            print("------------------------------")
        
        if page_num < total_pages:
            next_page = input("Press Enter to view next page or type 'q' to quit: ").strip().lower()
            if next_page == 'q':
                break
            page_num += 1
        else:
            break
    
    return True


