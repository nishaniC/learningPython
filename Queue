class QueueError(IndexError ):  # Choose base class for the new exception.
    def __init__(self):
        IndexError.__init__(self)
        # print("Queue error")


class Queue:
    def __init__(self):
        self.__queue=[]

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        try:
            vlaue=self.__queue[0]
            del self.__queue[0]
            return vlaue
        except:
            object_QueueError = QueueError()
            raise object_QueueError
        


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
# for i in range(4):
#     print(que.get())

try:
    for i in range(4):
        print(que.get())
except :
    print("Queue error")




#checks empty before getting
#checks empty before getting
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []
    def put(self,elem):
        self.__queue.insert(0,elem)
    def get(self):
        if len(self.__queue) > 0:
            elem = self.__queue[-1]
            del self.__queue[-1]
            return elem
        else:
            raise QueueError



class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.__empty=True
        
    def put(self,elem):
        self.__empty=False
        Queue.put(self,elem)

    def isempty(self):
        if (len(self._Queue__queue) == 0):
            self.__empty=True
        return self.__empty
        

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
