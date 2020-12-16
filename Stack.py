from LinkedList import DoubleLinkedList


class Stack:  # LIFO - Last in first out
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        var = self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size


my_stack = Stack()
my_stack.push(2)
my_stack.push(1)
my_stack.push(5)
print(len(my_stack))
print(my_stack.peek())
print(my_stack.pop())
print(len(my_stack))
