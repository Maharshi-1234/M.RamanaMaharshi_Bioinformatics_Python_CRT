#Write a Python Program to create a Mobile Class and Declare the States of Mobile as Color,Price,Brand,Series,Version,Features,
# Storage,Battery Capacity,RAM,Processor
#Create 10 Objects and initialse using constructor print the details of the Individual Object using function
class Mobile():
    def __init__(self,Color,Price,Brand,Series,Version,Features,Storage,Battery_Capacity,RAM,Processor):
        print("Objects are Created!")
        self.color = Color
        self.Price = Price
        self.Brand = Brand
        self.Series = Series
        self.Version = Version
        self.Features = Features
        self.Storage = Storage
        self.Battery_Capacity = Battery_Capacity
        self.RAM = RAM
        self.Processor = Processor
def displayDetails(self):
    print(f"Mobile Color : {E1.color}")
    print(f"Price        : {E1.Price}")
    print(f"Brand        : {E1.Brand}")
    print(f"Series       : {E1.Series}")
    print(f"Version      : {E1.Version}")
    print(f"Features     : {E1.Features}")
    print(f"Storage      : {E1.Storage}")
    print(f"Battery_Capacity  :  {E1.Battery_Capacity}")
    print(f"RAM          : {E1.RAM}")
    print(f"Processor    : {E1.Processor}")
E1= Mobile("Green","29,000","Samsung","S21","Fan Edition","64 MP Camera","128GB","4500mAh","8GB(+4GB Extendable)","SnapDragon 888")
displayDetails(E1)