#Queue Implementation using list
from collections import deque
queue=deque()

#Queue enqueue operation
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueue operation:",queue)

#Queue dequeue operation
if queue:
    dequeue=queue.popleft()
    print("Dequeued element from queue:",dequeue)
    print("Queue after dequeue operation:",queue)
else:
    print("Queue is empty!")

#Access top element from queue(Peek operation)
if queue:
    print("Top element of queue:",queue[0])
else:
    print("Queue is empty!")
