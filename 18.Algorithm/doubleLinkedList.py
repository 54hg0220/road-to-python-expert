class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, val):
        self.head = val
        self.tail = None
        self.length = 1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return True

    def pop(self):
        if self.length is 0:
            return None
        if self.length is 1:
            self.tail = None
            self.head = None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length is 0:
            return None
        if self.length is 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(self.length):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, self.length, -1):
                temp = temp.prev
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index - 1)
            after = before.next
            new_node.next = after
            new_node.prev = before
            before.next = new_node
            after.prev = new_node
            self.length += 1
            return True

    def delete(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
