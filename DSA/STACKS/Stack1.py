class Stack:
    def __init__(self):
        self.Stack = []

    def push(self, data):
        self.Stack.append(data)
        print(f"{data} element is appended")

    def isempty(self):
        return len(self.Stack) == 0

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            removed = self.Stack.pop()
            print(f"{removed} element is removed")

    def peak(self):
        length = len(self.Stack)
        if length > 0:
            print(f"The peak element is: {self.Stack[length - 1]}")
        else:
            print("Stack is empty.")

    def Display(self):
        for i in self.Stack:
            print(i)

# Using the stack
stack = Stack()
stack.push(100)
stack.push(105)
stack.push(150)
stack.push(78)
stack.peak()
stack.Display()