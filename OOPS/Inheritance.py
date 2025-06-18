#Operator Overloading : A Single Operator Performing Different Operations based on the datatype.
#Performing single task in  multiple ways

#Single level inheritance
class Vehicle:
    def __init__(self):
        print("I'm the Vehicle Class Constructor")
    @staticmethod
    def Start():
        print("Vehicle is Started")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("I'm the Car Class constructor")
    @staticmethod
    def Start():
        print("Car is Started")
C1=Car()
C1.Start()