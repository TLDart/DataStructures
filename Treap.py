from BSTree import BinarySearchTree
from TreeNode import TreeNode
import random

class Treap(BinarySearchTree):
    def __init__(self, substructure, root=None):
        """
            Initiates the BSTree, Defaults for maxHeap
        :param substructure: substructure used in the AVL Tree nodes
        :param root: root of the AVLTree
        """
        super().__init__(substructure, root)

    def add(self, node, lines=None):
        """
            Adds an element to the tree
        :param node: node to be added (can also add int)
        :param lines: lines to be added corresponding to the node
        :return: --
        """
        new = node if isinstance(node, TreeNode) else TreeNode(node, self.substructure(self.substructure))
        new.key = random.random()
        if lines:
            for line in lines:
                new.lines.add(line)

        if self.root:
            self.root = self.root.add(new, self.balancer)
            self.root.red = False
        else:
            self.root = new
            self.root.red = False

    def balancer(self, root, node):
        """
            Balancing function used in the SplayTree
        :param root: node to be worked in
        :param node: copy of the node used (needed to keep track of operations when going up in recursion
        :return: balanced
        """
        return root.maxHeapify(self.rotations)


class MaxTreap(Treap):
    def __init__(self, substructure, root=None):
        """
            Initiates a maxHeap
        :param substructure: substructure used in the AVL Tree nodes
        :param root: root of the AVLTree
        """
        super().__init__(substructure, root)


class MinTreap(BinarySearchTree):
    def __init__(self, substructure, root=None):
        """
            Initiates the Initiates a minHeap
        :param substructure: substructure used in the AVL Tree nodes
        :param root: root of the AVLTree
        """
        super().__init__(substructure, root)

    def balancer(self, root, node):
        """
            Balancing function used in the SplayTree
        :param root: node to be worked in
        :param node: copy of the node used (needed to keep track of operations when going up in recursion
        :return: balanced
        """
        return root.minHeapify(self.rotations)

if __name__ == '__main__':
    trp = Treap(Treap)
    arr2 = [10, 11, 8, 9, 7, 20, 12, 4, 2, 5]
    for i in arr2:
        trp.add(i)
    print("lol")
