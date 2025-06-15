class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursively(node.left, value)
        else:
            node.right = self._insert_recursively(node.right, value)
        return node

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursively(node.left, value)
        return self._search_recursively(node.right, value)

    def inorder_traversal(self):
        return self._inorder_recursively(self.root)

    def _inorder_recursively(self, node):
        if node is None:
            return []
        return (
            self._inorder_recursively(node.left)
            + [node.value]
            + self._inorder_recursively(node.right)
        )

    def preorder_traversal(self):
        return self._preorder_recursively(self.root)

    def _preorder_recursively(self, node):
        if node is None:
            return []
        return (
            [node.value]
            + self._preorder_recursively(node.left)
            + self._preorder_recursively(node.right)
        )

    def postorder_traversal(self):
        return self._postorder_recursively(self.root)

    def _postorder_recursively(self, node):
        if node is None:
            return []
        return (
            self._postorder_recursively(node.left)
            + self._postorder_recursively(node.right)
            + [node.value]
        )

    def height(self):
        return self._height_recursively(self.root)

    def _height_recursively(self, node):
        if node is None:
            return -1
        left_height = self._height_recursively(node.left)
        right_height = self._height_recursively(node.right)
        return max(left_height, right_height) + 1

    def is_balanced(self):
        return self._is_balanced_recursively(self.root)

    def _is_balanced_recursively(self, node):
        if node is None:
            return True
        left_height = self._height_recursively(node.left)
        right_height = self._height_recursively(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self._is_balanced_recursively(
            node.left
        ) and self._is_balanced_recursively(node.right)
