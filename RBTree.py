from BSTree import BinarySearchTree


class RBTree(BinarySearchTree):
    def __init__(self, substructure, root=None):
        """
            Initiates the RBTree
        :param substructure: substructure used in the RB Tree nodes
        :param root: root of the RBTree
        """
        super().__init__(substructure, root)

    def balancer(self, root, node):
        """
            Balancing function used in AVL Tree
        :param root: node to be worked in
        :param node: copy of the node used (needed to keep track of operations when going up in recursion
        :return: balanced
        """
        if root.left and root.left.red and root.right and root.right.red and (root.right.right and root.right.right.red or root.right.left and root.right.left.red or root.left.right and root.left.right.red or root.left.left and root.left.left.red):
            root.red = True
            root.left.red = False
            root.right.red = False
            return root
        elif root.left and root.left.red:
            if root.left.left and root.left.left.red:
                root.left.red = False
                root.red = True
                return root.rotateRight(self.rotations)
            elif root.left.right and root.left.right.red:
                root.left = root.left.rotateLeft(self.rotations)
                root.left.red = False
                root.red = True
                return root.rotateRight(self.rotations)
        elif root.right and root.right.red:
            if root.right.right and root.right.right.red:
                root.right.red = False
                root.red = True
                return root.rotateLeft(self.rotations)
            elif root.right.left and root.right.left.red:
                root.right = root.right.rotateRight(self.rotations)
                root.right.red = False
                root.red = True
                return root.rotateLeft(self.rotations)
        return root


if __name__ == '__main__':
    rbt = RBTree(RBTree)
    arr2 = [10, 11, 8, 9, 7]
    for i in arr2:
        rbt.add(i)
    print("lol")