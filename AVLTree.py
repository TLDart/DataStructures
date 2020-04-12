from BSTree import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self, substructure, root=None):
        """
            Initiates the AVLTree
        :param substructure: substructure used in the AVL Tree nodes
        :param root: root of the AVLTree
        """
        super().__init__(substructure, root)

    def balancer(self, root, node):
        """
            Balancing function used in AVL Tree
        :param root: node to be worked in
        :param node: copy of the node used (needed to keep track of operations when going up in recursion
        :return: balanced
        """
        ef = root.EF()
        # print(f"{self},{ef}")
        if ef > 1:
            bl = root.left.left.height() if root.left.left else -1
            br = root.left.right.height() if root.left.right else -1
            if bl > br:
                return root.rotateRight(self.rotations)
            else:
                root.left = root.left.rotateLeft(self.rotations)
                return root.rotateRight(self.rotations)
        if ef < -1:
            bl = root.right.left.height() if root.right.left else -1
            br = root.right.right.height() if root.right.right else -1
            if br > bl:
                # print("Here")
                return root.rotateLeft(self.rotations)
            else:
                # print("There")
                root.right = root.right.rotateRight(self.rotations)
                return root.rotateLeft(self.rotations)
        return root


if __name__ == '__main__':
    avl = AVLTree(AVLTree)
    avl.add(10)
    avl.add(7)
    avl.add(8)
    test = avl.get(7)
    test.lines.add(2)
    print("kek")

