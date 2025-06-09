# Linked List Implementation in Python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)  # Initialize with a dummy node
        self.head = new_node
        self.tail = new_node  # Keep track of the tail for O(1) append operations
        self.length = 1  # Keep track of the length of the linked list

    # Insert at the end of the linked list
    # O(n) if we traverse the list to find the last node, O(1) if we keep track of the last node.


    #  Insert at the beginning of the linked list
    # O(1) operation since we just need to change the head pointer.
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    


    # Delete a node by value
    # O(n) operation since we may need to traverse the entire list to find the node.


    # Search for a node by value
    # O(n) operation since we may need to traverse the entire list to find the node.

    
    # Insert a node after a specific node
    # O(n) operation since we may need to traverse the list to find the node after which to insert.

    
    # Insert a node before a specific node
    # O(n) operation since we may need to traverse the list to find the node before which to insert.

    # Print the linked list
    # O(n) operation since we need to traverse the entire list to print all elements.
    def print_list(self):

        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Linked List vs Lists
# Append operation in linked list is O(1) if we keep track of the last node.
# Lists in Python are dynamic arrays, which means appending is O(1) on average,
# Pop operation is O(n) if we remove from the start, but O(1) if we remove from the end.
# Linked lists allow for O(1) insertions and deletions at both ends, but require O(n) to access an element by index.
# Lookups in linked lists are O(n) since we have to traverse the list, while lists allow O(1) access by index.
# Lookups in Lists are O(1) since they are implemented as dynamic arrays.
my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.print_list()  # Output: 10 -> 20 -> None