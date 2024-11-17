import json

# def search_job_by_company_partial(company_name_input):
#     job_list = []
#     with open('database/job.txt', 'r') as file:
#         for line in file:
#             data = line.strip().split(',')
            
#             if company_name_input.lower() in data[1].strip().lower():
#                 job_info = {
#                     'job_no': data[0].strip(),
#                     'company_name': data[1].strip(),
#                     'email': data[2].strip(),
#                     'job_type': data[3].strip(),
#                     'contact': data[4].strip()
#                 }
#                 job_list.append(job_info)

#     return job_list

# company_name_input = input("Enter a keyword for company name to search: ").strip().lower()

# jobs = search_job_by_company_partial(company_name_input)
# if jobs:
#     jobs_json = json.dumps(jobs, indent=4)
#     print(jobs_json)
# else:
#     print(f"No jobs found for companies containing '{company_name_input}'.")

# def search_job_by_job_partial(job_name_input):
#     job_list = []
#     with open('database/job.txt', 'r') as file:
#         for line in file:
#             data = line.strip().split(',')
            
#             if job_name_input.lower() in data[3].strip().lower():
#                 job_info = {
#                     'job_no': data[0].strip(),
#                     'company_name': data[1].strip(),
#                     'email': data[2].strip(),
#                     'job_type': data[3].strip(),
#                     'contact': data[4].strip()
#                 }
#                 job_list.append(job_info)

#     return job_list

# job_name_input = input("Enter a keyword for job name to search: ").strip().lower()

# jobs = search_job_by_job_partial(job_name_input)
# if jobs:
#     jobs_json = json.dumps(jobs, indent=4)
#     print(jobs_json)
# else:
#     print(f"No jobs found for companies containing '{job_name_input}'.")
