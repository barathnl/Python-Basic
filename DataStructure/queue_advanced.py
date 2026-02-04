## Queue - First In First Out (FIFO)

# Deque is Double ended queue
from collections import deque
q = deque()

# Adding to end of queue
q.append('a')
q.append('b')
q.append('c')

# Removing from start of queue
print(q.popleft())
print(q.popleft())
print(q.popleft())

# Thread safe Queue
from queue import Queue
q = Queue(maxsize=3)

# Adding to end of queue
q.put('a')
q.put('b')
print(f"Current queue size {q.qsize()}")
q.put('c')

print(f"Is queue full : {q.full()}")

# Removing from start of queue
print(q.get())
print(q.get())
print(q.get())

print(f"Is queue empty : {q.empty()}")
