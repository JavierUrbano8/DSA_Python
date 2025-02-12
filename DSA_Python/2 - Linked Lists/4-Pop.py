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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


'EXAMPLE'
my_linked_list = LinkedList(1)
my_linked_list.append(9)

my_linked_list.print_list()
"Expected: 1 5 9"


print(my_linked_list.pop(), my_linked_list.pop(), my_linked_list.pop())

"""
Expected: 0x000..., 0x0000..., None because it returns the node we just pop()

If change *return temp* en pop() --> *return temp.value()*
Expected: 9, 1, None because it returns the value of the element popped from the LL
"""
