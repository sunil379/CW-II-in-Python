# rating the employee between 1-5
name = ["Sunil","Rits","Yash","Ayush"]
l = len(name)
def eom(emp_name):
    grade = []
    for i in range(l):
        print("Enter the grade of ",emp_name[i])
        p = input("Performance ")
        q = input("Quality of work ")
        a = input("Attendance ")
        b = input("Behaviour ")
        grade.insert(i,p+q+a+b)
    k  = grade.index(max(grade))
    return k    
result = eom(name)
print(f"Employee of the Month is {name[result]}")