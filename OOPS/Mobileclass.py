class Mobile():
    def __init__(self,P,C,B):
            self.Price=P
            self.Color=C
            self.Brand=B 
            print("Object is created")
    #Mutator
    def Set_Color(self):
          self.Color="Blue"
    #Accessor
    def Get_Details(self):
          print(f"Color : {self.Color}")
          print(f"Price : {self.Price}")
          print(f"Brand : {self.Brand}")
M1=Mobile(11000,'red','Samsung')
M1.Set_Color()
M1.Get_Details()