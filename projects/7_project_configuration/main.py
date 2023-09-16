import os

#TODO: Check user devgroup. If group not available create it. (write it in log file).
group_name = "devops"

user_name = "aws"

def generate_line_that_equal(group_name, group_list):
    for line in group_list:
        if line.strip().startswith(group_name) == True:
            yield line  

with open("/etc/group") as group_list:
    for line in generate_line_that_equal(group_name, group_list):
        print(line)



#TODO: Check user devadmin. If user not available create it. (write it in log file).
#TODO: Check user is added in devgroup. If user is not in group then add it. (write it in log file).



#forwardair_project_dir = "/usr/local/forwardair"
#forwardair_log_dir = "/var/log/forwardair"

#TODO: Check forwardair dir (project). If directory not available create it then set chwon and chmod. (write it in log file).
#TODO: Check forwardair dir (log). If directory not available create it then set chwon and chmod. (write it in log file).


#create_project_fa_dir = os.mkdir(project_parent_dir)

#print(create_project_fa_dir)
