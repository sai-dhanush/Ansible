class Employee:
    empid=''
    empName=''
    empDept=''

    def __init__(self,empid,empName,empDept):
        self.empDept=empDept
        self.empid=empid
        self.empName=empName

    def __str__(self):
        return f"Emploee Details: {self.empid} : {self.empName} {self.empDept}"
        

employee= Employee('e201','name','IT')
employee1= Employee('e202','name2','IT')
# employee.empDept='IT'
# employee.empid='e201'
# employee.empName="name"

print(employee.empid)
print(employee.empName)
print(employee.empDept)

print(employee)
print(employee1)