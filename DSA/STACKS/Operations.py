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
    def Display(self):
        self.Stack.reverse()
        str=[]
        for i in self.Stack:
            str.append(i)
        rev_str="".join(str)
        print(rev_str)
        
# Using the stack
stack = Stack()
stack.push('R')
stack.push('A')
stack.push('M')
stack.push('S')
stack.Display()