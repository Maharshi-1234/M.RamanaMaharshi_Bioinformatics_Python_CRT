#write a python prog to create a student class and declare the properties as student name, student id, branch, percentage, age, 
#paasing out year, certificate count,
#create 10 objects and initialize the values using mutator method and access them using accessor method
#NOTE:(You have to intialize the values without using constructors)
class Students():
    def __init__(self,Student_Name,Student_Id,Branch,Percentage,Age,Passing_year,Certificate_Count):
        self.Student_Name = Student_Name
        self.Student_Id = Student_Id
        self.Branch = Branch
        self.Percentage = Percentage
        self.Age = Age
        self.Passing_Year = Passing_year
        self.Certificate_Count = Certificate_Count
    def set_modify_details(self):
        self.Student_Name = "Lalasa"
        self.Student_Id = "221FA14046"
        self.Branch = "Bi"
        self.Percentage = "92%"
        self.Age = "5"
        self.Passing_Year = "2026"
        self.Certificate_Count = 0
    def get_details(self):
        print(f"Name of Student:{self.Student_Name}")
        print(f"Id of Student:{self.Student_Id}")
        print(f"Branch of Student:{self.Branch}")
        print(f"Percentage of Student:{self.Percentage}")
        print(f"Age of Student is :{self.Age}")
        print(f"Passing Year of Student is:{self.Passing_Year}")
        print(f"Certificates of std:{self.Certificate_Count}")
S1=Students("Lalasa", "221FA14046", "Bi", 100, 22, 2026, 44)
S1.set_modify_details()
S1.get_details()
S1.set_modify_details()
S1.get_details()