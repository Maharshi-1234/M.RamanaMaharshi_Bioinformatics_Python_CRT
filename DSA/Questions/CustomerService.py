'''Write a Python Program to create a Customer Service by Adding a Customer into the Queue and Once Customer is 
Served he has to be removed from the Queue'''
from collections import deque
queue = deque()
'''
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueuing:",queue)
first = queue.popleft()
print("Dequeued element:",first)
print("Queue after dequeuing:",queue)
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Front element:",queue[0])
'''

num = int(input("Number of customers at Customer Service: "))
for i in range (num):
    temp = input("Enter the customer name: ")
    queue.append(temp)
print(" **After Service** ")
for i in range(num):
    t = queue.popleft()
    print(f"Customer {i+1} received the Service")
print("Not empty") if bool(queue) else print("Queu is Empty after Completion of Service")