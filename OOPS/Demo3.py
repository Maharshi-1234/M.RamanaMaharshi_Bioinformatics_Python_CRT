class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
        print("Object is Created")
        self.Employee=empname
        self.empID=empID
        self.Designation=designation
        self.Salary=salary
        self.DeptName=deptname
def Display_Details(self):
    print(f"Employee Name :        {E1.Employee}")
    print(f"Employee ID :          {E1.empID}")
    print(f"Employee Designation : {E1.Designation}")
    print(f"Employee Salary :      {E1.Salary}")
    print(f"Department Name :      {E1.DeptName}")
E1=Employee('Ram','123','Data Analyst',45000,'Deployment team')
Display_Details(E1)