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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index not in range(self.length):
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp.value:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index not in (range(self.length)):
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            before = self.get(index-1)
            after = before.next
            before.next = new_node
            new_node.prev = before
            after.prev = new_node
            new_node.next = after
            self.length += 1
            return True

    def delete(self, index):
        if index not in range(self.length):
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


'EXAMPLE'
my_linked_list = DoublyLinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)


print("Complete list")
my_linked_list.print_list()
" Expected: {1, 2, 3, 4}"
my_linked_list.delete(2)
print("1st delete = ")
my_linked_list.print_list()
"Expected: 1st delete {1, 2, 4}"
my_linked_list.delete(0)
print("2nd delete = ")
my_linked_list.print_list()
" Expected: 2nd delete {2, 4}"
