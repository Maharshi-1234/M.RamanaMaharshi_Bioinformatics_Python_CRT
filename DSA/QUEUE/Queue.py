class Queue:
    def __init__(self):
        self.items = []
    # Add item to rear (end)
    def enqueue(self, item):
        self.items.append(item)
    # Remove and return the front item
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    # Look at the rear item without removing
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.items[-1]
    # Look at the front item without removing
    def peek_front(self):
        if self.is_empty():
            return None
        return self.items[0]
    # Check if queue is empty
    def is_empty(self):
        return len(self.items) == 0
    # Return the size of the queue
    def size(self):
        return len(self.items)
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Front:", q.peek_front())
print("Rear:", q.peek_rear())