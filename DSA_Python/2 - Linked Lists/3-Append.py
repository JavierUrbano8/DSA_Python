class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


'EXAMPLE'
my_linked_list = LinkedList(1)
my_linked_list.append(5)

print('Head:', my_linked_list.head.value,
      ', Tail:', my_linked_list.tail.value,
      ' Length:', my_linked_list.length)

"Expected: Head: 1 , Tail: 5  Length: 2"

my_linked_list.print_list()

"Expected 1 5"
