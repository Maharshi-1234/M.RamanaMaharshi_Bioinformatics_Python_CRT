#You have attended a Skill Development Training Program for 15 Days on Python Programming Language
#Task: Write a python Program to give a detailed report of 15 days python training which includes:
#1)Day
#2)Topics Covered
#3)Efficiency(Rate of Efficiency and Grip on topica learnt on a scale of 5)
#4)Number of Assignment Questions Solved
#5)Number of Hackerank Programs Solved
#6)Ratings Achieved on Hackerrank for that Particular Day
#7)Certifications Completed (including name of Certificate)
#8)Duration of Class
#9)Rate the Session on a Scale of 5 where
#   a)1-Being Worst
#   b)2-Being Bad
#   c)3-Being Average
#   d)4-Being Good 
#   e)5-Very Good
class SDT():
    def __init__(self,Day,Topics_Covered,Efficiency,AS_QUE,HR_QUE,Ratings_particularday,Certifications,Duration,Session_Rating):
        print("Objects are Created")
        self.Day = Day
        self.Topics_Covered = Topics_Covered
        self.Efficiency = Efficiency
        self.AS_QUE = AS_QUE
        self.HR_QUE = HR_QUE
        self.Ratings = Ratings_particularday
        self.Certifications = Certifications
        self.Duration = Duration
        self.Ratings = Session_Rating
def DetailedReport(self):
     print(f"Day : {E1.Day}")
     print(f"Topics_Covered : {E1.Topics_Covered}")
     print(f"Efficiency : {E1.Efficiency}")
     print(f"AS_QUE : {E1.AS_QUE}")
     print(f"HR_QUE : {E1.HR_QUE}")
     print(f"Ratings : {E1.Ratings}")
     print(f"Cerifications : {E1.Certifications}")
     print(f"Duration : {E1.Duration}")
     print(f"Ratings : {E1.Ratings}")
def DetailedReport2(self):
     print(f"Day : {E2.Day}")
     print(f"Topics_Covered : {E2.Topics_Covered}")
     print(f"Efficiency : {E2.Efficiency}")
     print(f"AS_QUE : {E2.AS_QUE}")
     print(f"HR_QUE : {E2.HR_QUE}")
     print(f"Ratings : {E2.Ratings}")
     print(f"Cerifications : {E2.Certifications}")
     print(f"Duration : {E2.Duration}")
     print(f"Ratings : {E2.Ratings}")
E1 = SDT("14","Basics,Operators,Functions,Strings","4","6","10","4","You have been Python Certified!","11 Days","4")
E2 = SDT("8","Functions,Strings,Dictionary","3","7","17","4","You are doing Good!Keep up with same pace to earn a Certificate!","9 Days","5")
DetailedReport(E1)
DetailedReport2(E2)