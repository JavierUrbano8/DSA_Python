class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(linked_list, k):
    slow = linked_list.head
    fast = linked_list.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


result = find_kth_from_end(my_linked_list, 2)
print(result.value)  # Output: 4
result = find_kth_from_end(my_linked_list, 1)
print(result.value)  # Output: 5

'Edge Case: First element of the list (already did not understand it)'
result = find_kth_from_end(my_linked_list, 5)
print(result.value)  # Output: 1

"""
    EXPECTED OUTPUT:
    ----------------
    4, 5, 1
    
"""
