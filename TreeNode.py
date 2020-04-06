from Node import Node


class TreeNode(Node):
    def __init__(self, data, lines=None, left=None, right=None):
        super(TreeNode, self).__init__(data, lines)
        self.left = left
        self.right = right
        self.red = True
        self.parent = None

    def __contains__(self, node):
        if node.data == self.data:
            return True
        elif node.data > self.data:
            return False if self.right is None else node in self.right
        else:
            return False if self.left is None else node in self.left

    def height(self):
        if self.right is None and self.left is None:
            return 1
        elif self.right is None:
            return 1 + self.left.height()
        elif self.left is None:
            return 1 + self.right.height()
        else:
            return 1 + max(self.right.height(), self.left.height())

    def EF(self):
        if self.right is None and self.left is None:
            return 0
        elif self.right is None:
            return self.left.height()
        elif self.left is None:
            return -self.right.height()
        else:
            return self.left.height() - self.right.height()

    def add(self, node, balancer):
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
        new = self.left
        new.parent = self.parent
        if new.right:
            new.right.parent = self
        self.left = new.right
        self.parent = new
        new.right = self

        if not isinstance(self.data, int):
            rotations[0] += 1
        return new

    def rotateLeft(self, rotations):  # With right child
        new = self.right
        new.parent = self.parent
        if new.left:
            new.left.parent = self
        self.right = new.left
        self.parent = new
        new.left = self

        if not isinstance(self.data, int):
            rotations[0] += 1
        return new

    def InOrder(self, order):
        if self.left:
            self.left.InOrder(order)
        order.append(self.data)
        if self.right:
            self.right.InOrder(order)

    def PreOrder(self, order):
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
        if node.data == self.data:
            return self
        elif node.data > self.data:
            return None if self.right is None else self.right.get(node)
        else:
            return None if self.left is None else self.left.get(node)

