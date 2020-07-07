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
        hL = root.left.height if root.left else 0
        hR = root.right.height if root.right else 0
        root.height = 1 + max(hL, hR)

        ef = root.EF()
        # print(f"{self},{ef}")
        if ef > 1:
            bl = root.left.left.height if root.left.left else -1
            br = root.left.right.height if root.left.right else -1
            if bl > br:
                return root.rotateRight(self.rotations)
            else:
                root.left = root.left.rotateLeft(self.rotations)
                return root.rotateRight(self.rotations)
        if ef < -1:
            bl = root.right.left.height if root.right.left else -1
            br = root.right.right.height if root.right.right else -1
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
    test2 = [40, 56, 84, 50, 29, 14, 91, 39, 21, 36]
    for i in test2:
        avl.add(i)

    #test = avl.get(7)
    #test.lines.add(2)
    print("kek")

