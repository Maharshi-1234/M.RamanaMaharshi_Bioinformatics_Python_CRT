#Node class single linkedlist 
class Node():
    def __init__(self,data):
        self.Data=data
        self.Next=None
First=Node(10)
Second=Node(20)
Third=Node(30)
Fourth=Node(40)
Fifth=Node(50)
Sixth=Node(60)
Seventh=Node(70)
Eighth=Node(80)
Ninth=Node(90)
head=First
head.Next=Second
Second.Next=Third
Third.Next=Fourth
Fourth.Next=Fifth
Fifth.Next=Sixth
Sixth.Next=Seventh
Seventh.Next=Eighth
Eighth.Next=Ninth
Current=head
while Current:
    print(Current.Data,end=" -> ")
    Current = Current.Next
print("None")