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
        #print(new.data, new.key)
        if lines:
            for line in lines:
                new.lines.add(line)

        if self.root:
            self.root = self.root.add(new, self.balancer)
            self.root.red = False
        else:
            self.root = new
            self.root.red = False


class MaxTreap(Treap):
    def __init__(self, substructure, root=None):
        """
            Initiates a maxHeap
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
        if root.left:
            if root.left.data == node.data:
                if root.key < node.key:
                    return root.rotateRight(self.rotations)

        if root.right:
            if root.right.data == node.data:
                if root.key < node.key:
                    return root.rotateLeft(self.rotations)
        return root



class MinTreap(Treap):
    def __init__(self, substructure, root=None):
        """
            Initiates minTreap
        :param substructure: substructure used in the AVL Tree nodes
        :param root: root of the AVLTree
        """
        super().__init__(substructure, root)

    def balancer(self, root, node):
        """
            Balancing function used in the MinTreap
        :param root: node to be worked in
        :param node: copy of the node used (needed to keep track of operations when going up in recursion
        :return: balanced
        """
        if root.left:
            if root.left.data == node.data:
                if root.key > node.key:
                    return root.rotateRight(self.rotations)

        if root.right:
            if root.right.data == node.data:
                if root.key > node.key:
                    return root.rotateLeft(self.rotations)
        return root


if __name__ == '__main__':
    trp = MaxTreap(MaxTreap)
    arr2 = [10, 2, 7, 9, 16, 1, 3, 12, 15, 4, 5, 17, 20, 8, 14, 11, 18, 6, 19, 13]
    for i in arr2:
        trp.add(i)
    print("lol")
