from Node import Node


class TreeNode(Node):
    def __init__(self, data, lines=None, left=None, right=None):
        """
            Initializes the tree node
        :param data: data
        :param lines: DataStructure used in the supplemental tree
        :param left: left child of the node
        :param right: right child of the node
        """
        super(TreeNode, self).__init__(data, lines)
        self.left = left
        self.right = right
        self.height = 1
        self.red = True
        self.parent = None
        self.key = 0

    def __contains__(self, node):
        """
            Verifies if a node is in tree
        :param node: node to be searched
        :return: False if the node is not false, else True
        """
        if node.data == self.data:
            return True
        elif node.data > self.data:
            return False if self.right is None else node in self.right
        else:
            return False if self.left is None else node in self.left

    def EF(self):
        """
            Calculates the equilibrium factor in the node (used in AVL Tree)
        :return: equilibrium factor of a node
        """
        if self.right is None and self.left is None:
            return 0
        elif self.right is None:
            return self.left.height
        elif self.left is None:
            return - self.right.height
        else:
            return self.left.height - self.right.height

    def add(self, node, balancer):
        """
            Performs a binary search tree add and the then uses the balancer to the node
        :param node:
        :param balancer: balancing function applied to the node after the bst add
        :return: returns the tree with the balanced node
        """
        if self.data == node.data:
            raise ValueError
        if node.data > self.data:
            if self.right:
                self.right = self.right.add(node, balancer)
            else:
                self.right = node
                node.parent = self
        else:
            if self.left:
                self.left = self.left.add(node, balancer)
            else:
                self.left = node
                node.parent = self

        return balancer(self, node)

    def rotateRight(self, rotations):
        """
            Rotates self to the right whilst also adjusting the parent node
        :param rotations: used to count rotations
        :return: returns the rotated node
        """
        new = self.left
        new.parent = self.parent
        if new.right:
            new.right.parent = self
        self.left = new.right
        self.parent = new
        new.right = self

        self.height = 1 + max(self.right.height if self.right else 0,
                              self.left.height if self.left else 0)
        new.height = 1 + max(new.right.height if new.right else 0, new.left.height if new.left else 0)

        if not isinstance(self.data, int):
            rotations[0] += 1
        return new

    def rotateLeft(self, rotations):  # With right child
        """
            Rotates self to the left whilst also adjusting the parent node
        :param rotations: used to count rotations
        :return: returns the rotated node
        """
        new = self.right
        new.parent = self.parent
        if new.left:
            new.left.parent = self
        self.right = new.left
        self.parent = new
        new.left = self

        self.height = 1 + max(self.right.height if self.right else 0,
                              self.left.height if self.left else 0)
        new.height = 1 + max(new.right.height if new.right else 0, new.left.height if new.left else 0)


        if not isinstance(self.data, int):
            rotations[0] += 1
        return new

    def InOrder(self, order):
        """
        :param order: list that will hold all the values
        :return: Recursive function that fills the array with the items of the tree in Order
        """
        if self.left:
            self.left.InOrder(order)
        order.append(self.data)
        if self.right:
            self.right.InOrder(order)

    def PreOrder(self, order):
        """
        :param order: list that will hold all the values
        :return: Recursive function that fills the array with the items of the tree in Post Order
        """
        order.append(self.data)
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    def PostOrder(self, order):
        """
        :param order: list that will hold all the values
        :return: Recursive function that fills the array with the items of the tree in Post Order
        """
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        order.append(self.data)

    def get(self, node):
        """
            Searches for a node in the tree
        :param node: node to be searched
        :return: None if node is not found, else returns a copy of the node in the tree
        """
        if node.data == self.data:
            return self
        elif node.data > self.data:
            return None if self.right is None else self.right.get(node)
        else:
            return None if self.left is None else self.left.get(node)

