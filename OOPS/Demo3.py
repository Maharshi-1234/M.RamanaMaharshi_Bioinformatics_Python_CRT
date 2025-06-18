class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
        print("Object is Created")
        self.Employee=empname
        self.empID=empID
        self.Designation=designation
        self.Salary=salary
        self.DeptName=deptname
    def Get_details(self):
        print(self.Employee)
        print(self.empID)
        print(self.Designation)
        print(self.Salary)
E1=Employee('Ram','123','Data Analyst',45000,'Deployment team')
E1.Get_details()