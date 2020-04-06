from BSTree import BinarySearchTree
from TreeNode import TreeNode


class SplayTree(BinarySearchTree):
    def __init__(self, substructure, root=None):
        super().__init__(substructure, root)

    def balancer(self, root, node):
        if node.data > root.data:
            if root.right and node.data > root.right.data and root.right.right and node.data == root.right.right.data:
                root.rotateLeft(self.rotations)
                return root.parent.rotateLeft(self.rotations)
            elif root.right and node.data < root.right.data and root.right.left and node.data == root.right.left.data:
                root.right = root.right.rotateRight(self.rotations)
                return root.rotateLeft(self.rotations)
        else:
            if root.left and node.data < root.left.data and root.left.left and node.data == root.left.left.data:
                root.rotateRight(self.rotations)
                return root.parent.rotateRight(self.rotations)
            elif root.left and node.data > root.left.data and root.left.right and node.data == root.left.right.data:
                root.left = root.left.rotateLeft(self.rotations)
                return root.rotateRight(self.rotations)
        if not root.parent:
            if root.right and root.right.data == node.data:  # Node is to the left of the parent
                return root.rotateLeft(self.rotations)
            elif root.left and root.left.data == node.data:  # Node is to the left of parent
                return root.rotateRight(self.rotations)
        return root

    def findNSplay(self, root, node, balancer):
        if node.data == root.data:
            return root
        elif node.data > root.data:
            if root.right:
                # print("Recursed")
                root.right = self.findNSplay(root.right, node, balancer)
        else:
            if root.left:
                root.left = self.findNSplay(root.left, node, balancer)
        return balancer(root, node)

    def get(self, node):
        if self.root:
            new = node if isinstance(node, TreeNode) else TreeNode(node)
            self.root = self.findNSplay(self.root, new, self.balancer)
            return self.root if self.root == new else None
        else:
            return None

    def find(self, node):
        if self.root:
            new = node if isinstance(node, TreeNode) else TreeNode(node)
            return self.root.get(new)
        else:
            return None


if __name__ == '__main__':
    sp = SplayTree(SplayTree)
    sp.add(10)
    sp.add(12)
    sp.add(8)
    sp.add(11)
    sp.add(9)
    sp.get(9)
    print("eks mdee")