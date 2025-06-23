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
    def Check_Balance(self):
        if '([}' in self.Stack:
            if self.Stack[3:]=='{[(':
                print("Balanced Paranthesis")
            elif self.Stack[3:]==
# Using the stack
stack = Stack()
stack.push('([{}])')
stack.push('({{}})')
stack.push('{[{}]}')
stack.push('[{()}]')
stack.push('[{()}])')
stack.push('')