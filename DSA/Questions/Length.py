'''Write a Python Program to take the length of queue as a input from the user and add the elements by using enqueue method and 
print the Elements present in the queue and remove the elements one by one from the queue and check whether the 
queue is empty or not and print the front peek and rear peek.'''
from collections import deque
queue =  deque()

num = int(input("Number of Customers at Customer Service: "))
for i in range (num):
    temp = input("Enter the Customer Name: ")
    queue.append(temp)
print("First element in queue is: ",queue[0])
print("Last element in queue is: ",queue[len(queue)-1])
print(" **Dequeuing** ")
for i in range(num):
    t = queue.popleft()
    print(f"Element {i+1} is Popped")
print("Not empty") if bool(queue) else print("Empty")