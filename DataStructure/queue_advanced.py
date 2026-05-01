"""
PYTHON QUEUE INTERVIEW CHEAT SHEET
-----------------------------------------------------------------------
Property: FIFO (First-In, First-Out).

IMPLEMENTATION | MODULE             | BIG O (Push/Pop) | BEST USE CASE
-----------------------------------------------------------------------
deque          | collections        | O(1)             | BFS, General Queues.
Queue          | queue              | O(1)             | Multi-threaded apps.
list           | built-in           | O(n) for pop(0)  | NEVER use for queues.
-----------------------------------------------------------------------
"""
from collections import deque
from queue import Queue


def deque_revision():
    """
    Deque (Double-Ended Queue) is the standard for interview algorithms.
    It provides O(1) appends and pops from both ends.
    """
    print("--- collections.deque (High Performance) ---")
    message_queue = deque()

    # Adding to the end (Enqueue) - O(1)
    message_queue.append('request_a')
    message_queue.append('request_b')
    message_queue.append('request_c')

    # Adding to the front
    message_queue.appendleft('request_top')
    print(message_queue)

    # Removing from the start (Dequeue) - O(1)
    print(f"Processing: {message_queue.popleft()}")

    # Removing from the end
    print(f"Processing: {message_queue.pop()}")


def thread_safe_queue_revision():
    """
    queue.Queue is designed for multi-threading.
    It includes locking semantics to handle concurrent access.
    """
    print("\n--- queue.Queue (Thread-Safe) ---")
    # maxsize=0 means infinite, otherwise it blocks when full
    task_buffer = Queue(maxsize=3)

    # Adding to queue (put)
    task_buffer.put('task_1')
    task_buffer.put('task_2')
    print(f"Current size: {task_buffer.qsize()}")

    task_buffer.put('task_3')
    print(f"Is buffer full? {task_buffer.full()}")

    # Removing from queue (get)
    print(f"Executing: {task_buffer.get()}")
    print(f"Executing: {task_buffer.get()}")
    print(f"Executing: {task_buffer.get()}")

    print(f"Is buffer empty? {task_buffer.empty()}")


if __name__ == "__main__":
    deque_revision()
    thread_safe_queue_revision()