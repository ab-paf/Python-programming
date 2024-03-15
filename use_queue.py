
from module_queue import enqueue
from module_queue import dequeue
from module_queue import printq

queue = ["Eric", "John", "Michael"]
queue.append("Terry")
queue.append("Graham")


enqueue(queue)
dequeue(queue)
printq(queue)