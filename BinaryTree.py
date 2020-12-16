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


my_tree = BinaryTree()
for c in [3, 1, 2, 5, 6, 3, 9, 6, 33]:
    my_tree.insert(c)
    print(my_tree)
