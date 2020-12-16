from Stack import Stack
from BinaryTreePrinter import BinaryTreePrinter


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class BinarySearchTree:  # No Duplicate value and & left node will be smaller than root
    def __init__(self):
        self.root = None

    def __insert_value(self, node, value):
        if node.val == value:
            return
        elif value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.__insert_value(node.right, value)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert_value(self.root, val)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)

    def __in_order(self, node):
        if node is None:
            return
        self.__in_order(node.left)
        print(node.val, end=" ")  # Don't print in the new line
        self.__in_order(node.right)

    def in_order(self):  # In order traversal - Three type of three traversal
        # Inorder (Left, Root, Right)
        # Preorder (Root, Left, Right)
        # Postorder (Left, Right, Root)
        self.__in_order(self.root)

    def contains(self, val):  # DFS = Depth first search
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            node = nodes.pop()
            print("Checking Node:", node.val)
            if node.val == val:
                return True
            elif val < node.val:
                if node.left is not None:
                    nodes.push(node.left)
            else:
                if node.right is not None:
                    nodes.push(node.right)
        return False


bst = BinarySearchTree()
for i in [45, 8, 2, 1, 10, 100, 50, 40, 23, 16, 7]:
    bst.insert(i)
    print(bst)

bst.in_order()

print()
print("DFS Contains 16:", bst.contains(16))
print("DFS Contains 41:", bst.contains(41))
