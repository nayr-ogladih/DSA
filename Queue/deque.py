




from collections import deque

# collections.deque class as  FIFO

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)
print(customQueue.clear())
print(customQueue)


import queue as q
#que as FIFO

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())


from multiprocessing import Queue
# multiprocessing.Queue as a FIFO queue:

customQueue = Queue(maxsize=3)
customQueue.put(1)
print(customQueue.get())
