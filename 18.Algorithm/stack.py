class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        if self.height < 1:
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return False
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        self.top.next = None
        return temp


my_stack = Stack(4)
my_stack.push(1)
my_stack.push(2)

print(my_stack.pop().value)
