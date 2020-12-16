from LinkedList import DoubleLinkedList


class Queue:  # FIFO - First in first out
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self, val):
        self.__list.add(val)

    def dequeue(self):
        val = self.__list.front()
        self.__list.remove_first()
        return val

    def front(self):
        return self.__list.front()

    def is_empty(self):
        return self.__list.size == 0

    def __len__(self):
        return self.__list.size


# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(6)
# my_queue.enqueue(7)
# my_queue.enqueue(11)
# print(len(my_queue))
# print(my_queue.front())
# print(my_queue.dequeue())
