class Graduation():
    def __init__(self):
        print("hehe")
    #@staticmethod
    def Graduate(self):
        print("Congratulations! You are now a Graduate")
#First Sub Class
class CSE(Graduation):
    def __init__(self):
        super().__init__()
        print("haha")
    @staticmethod
    def Graduate():
        print("Congratulations! You are now a Computer Science Graduate")
#Second sub class
class BI(Graduation):
    def __init__(self):
        super().__init__()
        pass
    @staticmethod
    def Graduate():
        print("Congratulations! You are now a Bioinformatician Graduate")
#Third sub class
class ECE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations! You are now a ECE Graduate")
CSE.Graduate()
BI.Graduate()
ECE.Graduate()