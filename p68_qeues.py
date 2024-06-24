# qeues use the FIFO behaviour meaning First in Fist Out
# this means you remove the first item from the list
# this has an adverse effect of slowing the memory of the application because you have to move every item to the left
# imagine moving a million items to the left

# the solution to this is using a deque function from the collections module

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
queue.popleft()
print(queue)
