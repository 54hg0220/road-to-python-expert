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

    # Insert at the beginning of the linked list
    # O(1) operation since we just need to update the head pointer.
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # Insert at the end of the linked list
    # O(n) if we traverse the list to find the last node, O(1) if we keep track of the last node.
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
    
    # Pop the last node from the linked list
    def pop(self):
        if self.length == 0:
            return None
        current = self.head
        pre = self.head
        while current.next:
            pre = current
            current = current.next
        self.tail = pre  # Update the tail to the second last node
        pre.next = None  # Remove the last node
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current.value

    # Pop the first node from the linked list
    def pop_first(self):
        if self.length == 0:
            return None
        
        current = self.head
        pop_value = current.value
        # update cursor
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = current.next
            current.next = None
        self.length -= 1
        return pop_value
    # Delete a node by index
    # O(n) operation since we may need to traverse the entire list to find the node.
    def delete(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.pop_first()
            return True
        if index == self.length:
            self.pop()
            return True
        pre = self.get(index - 1)
        current = pre.next
        pre.next = current.next  # Bypass the current node
        current.next = None  # Clear the next pointer of the removed node
        self.length -= 1
        return current

    # Get a node by index
    # O(n) operation since we may need to traverse the list to find the node at the given index.
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # Set a node's value by index
    # O(n) operation since we may need to traverse the list to find the node at the given index.
    def set_value(self, index, value):
        current = self.get(index)
        if current is None:
            return False
        else:
            current.value = value
            return True
    
    # Insert a node after a specific node
    # O(n) operation since we may need to traverse the list to find the node after which to insert.
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        current = self.get(index - 1)
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return True
    
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

    # Leetcode 206: Reverse Linked List
    # O(n) operation since we need to traverse the entire list to reverse it.
    def reverse(self):
        current = self.head
        self.head = self.tail
        self.tail = current
        # starting from the head, we will reverse the pointers
        prev = None
        for _ in range(self.length):
            next = current.next # who is the next node
            current.next = prev # reverse the pointer
            prev = current # move prev to current
            current = next # move current to next

        return True

    # Leetcode 876:Find the middle of the linked list
    # O(n) operation since we need to traverse the entire list to find the middle node.
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Leetcode 141: Detect Cycle in Linked List
    # O(n) operation since we need to traverse the entire list to check for cycles.
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # Leetcode 2: Find the kth to last element in the linked list
    # O(n) operation since we need to traverse the entire list to find the kth to last element.
    # Using two pointers, one at the kth position and the other at the head.
    def find_kth_to_last(self, k):
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    # Leetcode 17: LL binary to decimal conversion
    # O(n) operation since we need to traverse the entire list to convert binary to decimal.
    def binary_to_decimal(self):
        current = self.head
        decimal_value = 0
        while current:
            decimal_value = decimal_value*2+ current.value
            current = current.next
        return decimal_value

    # Leet code 83: Remove Duplicates from Sorted List
    # O(n) operation since we need to traverse the entire list to remove duplicates.
    # use set to keep track of seen values
    # cannot use delete method
    # since we need to remove duplicates without knowing the index.
    def remove_duplicates(self):
        if self.head is None:
            return None
        current = self.head
        seen = set()
        seen.add(current.value)
        while current.next:
            if current.next.value in seen:
                # remove the next node
                current.next = current.next.next
                self.length -= 1
            else:
                seen.add(current.next.value)
                current = current.next
        return self.head

# Linked List vs Lists
# Append operation in linked list is O(1) if we keep track of the last node.
# Lists in Python are dynamic arrays, which means appending is O(1) on average,
# Pop operation is O(n) if we remove from the start, but O(1) if we remove from the end.
# Linked lists allow for O(1) insertions and deletions at both ends, but require O(n) to access an element by index.
# Lookups in linked lists are O(n) since we have to traverse the list, while lists allow O(1) access by index.
# Lookups in Lists are O(1) since they are implemented as dynamic arrays.
my_linked_list = LinkedList(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(30)
my_linked_list.print_list()  # Output: 10 -> 20 -> 30 -> None
my_linked_list.remove_duplicates()
my_linked_list.print_list()  # Output: 10 -> 20 -> 30 -> None
# print(my_linked_list.get(2).value)  # Output: 30
# my_linked_list.set_value(1, 25)
# my_linked_list.print_list()  # Output: 10 -> 25 -> 30 -> None
# my_linked_list.insert(1, 15)
# my_linked_list.print_list()  # Output: 10 -> 15 -> 25 -> 30 -> None
# my_linked_list.delete(1)
# my_linked_list.print_list()  # Output: 10 -> 25 -> 30 -> None
# print(my_linked_list.pop_first())  # Output: 10
# my_linked_list.print_list()  # Output: 20 -> 30 -> None
# print(my_linked_list.pop_first())  # Output: 20
# my_linked_list.print_list()  # Output: 30 -> None
# print(my_linked_list.pop())  # Output: 30
# my_linked_list.print_list()  # Output: 10 -> 20 -> None
# print(my_linked_list.pop())  # Output: 10
# my_linked_list.print_list()  # Output: None
my_linked_list2 = LinkedList(1)
my_linked_list2.append(2)
my_linked_list2.append(3)
my_linked_list2.append(4)
my_linked_list2.reverse()
print("Reversed Linked List:")
my_linked_list2.print_list()  # Output: 4 -> 3 -> 2 -> 1 -> None