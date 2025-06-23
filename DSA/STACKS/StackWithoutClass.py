from collections import deque
stack = deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after Pushing:", stack)
top = stack.pop()
print("Popped Element:", top)
print("Stack after Popping:", stack)
if not stack:
    print("Stack is empty")
else:
    print("Stack is not Empty")
print("Front Element:", stack[-1])