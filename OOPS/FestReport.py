#You had Participated in your College level coding fest which was there for 6 days
#Task : Write a python program to give the Final Report which includes 
#1.Activities for the day Including Timeline
#2.Number of teams/Partiicpants for the day
#3.Project_Names
#4.Technologies Used
#5.PPT Demonstration Given
#6.Winner of the Day
#7.Runner up of the Day
#8.Best Performer of the Day
#9.Host of the Program for the Day
class fest():
    def __init__(self,Activities_with_timeline,Number_of_Teams,Project_Names,Technologies_Used,Demonstration_Given,Winner,Runnerup,BestPerformer,Host):
        print("Objects are Created!")
        self.Activities_with_timeline = Activities_with_timeline
        self.Number_of_Teams = Number_of_Teams
        self.Project_Names = Project_Names
        self.Technologies = Technologies_Used
        self.Demonstration = Demonstration_Given
        self.Winner = Winner
        self.Runnerup = Runnerup
        self.BestPerformer = BestPerformer
        self.Host = Host
def FinalReport(self):
    print(f"Activities for Day      : {E1.Activities_with_timeline}")
    print(f"Number of Teams         : {E1.Number_of_Teams}")
    print(f"Project Names           : {E1.Project_Names}")
    print(f"Technologies Used       : {E1.Technologies}")
    print(f"PPT Demonstration Given : {E1.Demonstration}")
    print(f"Winner of the Day       : {E1.Winner}")
    print(f"Runner up of the Day    : {E1.Runnerup}")
    print(f"Best Performer of   Day : {E1.BestPerformer}")
    print(f"Host of The Program for the Day : {E1.Host}")
E1=fest("Welcome Dance : 09:00 AM","5","Machine Learning Using BioData","Python,Machine Learning Algorithms","PPT Demonstration with Images","Kethan","Jeswanth","Lalasa","Sriram")
FinalReport(E1)