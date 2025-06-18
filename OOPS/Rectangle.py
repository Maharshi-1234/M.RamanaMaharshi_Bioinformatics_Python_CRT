#Write a Python Program to create a Rectangle class and initialise the variables Len,Bre Using Constructors and access
#the values Using Mutator Methods
class Rectangle():
    def __init__(self,length,Breadth):
        self.Length = length
        self.Breadth = Breadth
        print("Objects are Created")
    def Set_Details(self):
        self.Length = self.Length
        print(f"length = {self.Length}")
        self.Breadth = self.Breadth
        print(f"Breadth = {self.Breadth}")
R=Rectangle(20,19)
R.Set_Details()