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


'EXAMPLE'
my_linked_list = DoublyLinkedList(7)
print('Head:', my_linked_list.head.value,
      ', Tail:', my_linked_list.tail.value,
      ' Length:', my_linked_list.length)

" Expected: 'Head: 2 , Tail: 2  Length: 1' "
