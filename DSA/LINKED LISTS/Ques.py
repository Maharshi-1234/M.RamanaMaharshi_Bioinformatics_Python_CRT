#Write a py program to create a linked list of size N take 
# the value of N as user input and data also
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def create_linked_list(n):
    if n <= 0:
        return None
    data = input("Enter data for node 1: ")
    head = Node(data)
    current = head
    for i in range(2, n+1):
        data = input(f"Enter data for node {i}: ")
        current.next = Node(data)
        current = current.next
    
    return head
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()
n = int(input("Enter the size of linked list: "))
head = create_linked_list(n)
print("Linked list:")
print_linked_list(head)
