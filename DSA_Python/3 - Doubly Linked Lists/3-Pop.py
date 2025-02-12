class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

        return temp


'EXAMPLE'
my_linked_list = DoublyLinkedList(7)
my_linked_list.append(19)
my_linked_list.append(232)
print("Complete list")
my_linked_list.print_list()
" Expected: {7, 19, 232}"
print("1st pop")
my_linked_list.pop()
my_linked_list.print_list()
" Expected: {7, 19}"
print("2nd pop")
my_linked_list.pop()
my_linked_list.print_list()
" Expected: {7}"
