# Binary tree

from Queue import Queue
from BinaryTreePrinter import BinaryTreePrinter


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                checking_node = nodes.dequeue()
                if checking_node.left is None:
                    checking_node.left = TreeNode(val)
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val)
                    return
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


class BinarySearchTree:  # No Duplicate value and & left node will be smaller than root
    def __init__(self):
        self.root = None

    def __insert_value(self, node, value):
        if node is None:
            return

        if node.val == value:
            return
        elif value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
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

# my_tree = BinaryTree()
# for c in [3,1,2,5,6,3,9,6,33]:
#     my_tree.insert(c)
#     print(my_tree)


bst = BinarySearchTree()
for i in [45, 8, 2, 1, 10, 100, 50, 40, 23, 16, 7]:
    bst.insert(i)
    print(bst)

bst.in_order()
