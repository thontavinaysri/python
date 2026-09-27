#25341a05l1 vinay

def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)



student_info("Vinay", 101, "CSE")
print()
student_info(branch="CSE", name="Vinay", roll_no=101)

'''output :
Name: Vinay
Roll No: 101
Branch: CSE

Name: Vinay
Roll No: 101
Branch: CSE
'''