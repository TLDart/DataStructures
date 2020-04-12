from Node import Node


class LinkedNode(Node):
    def __init__(self, data=None, lines=None, next=None):
        """
        :param data: data of the node
        :param lines: DataStructure used in the supplemental tree
        :param next: next element to the node
        """
        super().__init__(data, lines)
        self.next = next

    def __contains__(self, node):
        """
            Verifies if a node is in tree
        :param node: node to be searched
        :return: False if the node is not false, else True
        """
        if self.data == node.data:
            return True
        else:
            return False if not self.next else self.next.get(node)

    def add(self, node):
        """
            Performs an add to the linked node using the insertion sort
        :param node: node to be inserted
        :return: tree with inserted node
        """
        if self.next and self.next.data < node.data:
            return self.next.add(node)
        node.next = self.next
        self.next = node
        return node

    def get(self, node):
        """
            Retrieves a node from the tree
        :param node: node to be searched
        :return: None if the node is not found else returns a copy of a node
        """
        if self.data == node.data:
            return self
        else:
            return None if not self.next else self.next.get(node)

    def InOrder(self, order):
        """
            Prints the linked list
        :param order: list that the elements will be added to
        :return: --
        """
        order.append(self)
        if self.next:
            if self.next:
                self.next.InOrder(order)
