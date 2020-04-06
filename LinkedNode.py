from Node import Node


class LinkedNode(Node):
    def __init__(self, data=None, lines=None, next=None):
        super().__init__(data, lines)
        self.next = next

    def __contains__(self, node):
        if self.data == node.data:
            return True
        else:
            return False if not self.next else self.next.get(node)

    def add(self, node):
        if self.next and self.next.data < node.data:
            return self.next.add(node)
        node.next = self.next
        self.next = node
        return node

    def get(self, node):
        if self.data == node.data:
            return self
        else:
            return None if not self.next else self.next.get(node)

    def InOrder(self, order):
        order.append(self)
        if self.next:
            if self.next:
                self.next.InOrder(order)
