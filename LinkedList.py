from LinkedNode import LinkedNode


class LinkedList:
    def __init__(self, substructure, head=None):
        self.head = None
        self.substructure = substructure
        self.buildTree(head)
        self.rotations = [0]
        self.total = 0
        self.unique = 0

    def __repr__(self):
        return self.InOrder()

    def __contains__(self, node):
        new = node if isinstance(node, LinkedNode) else LinkedNode(node)
        return new in self.head

    def buildTree(self, elements):
        if elements is None:
            self.head = None
        else:
            for element in elements:
                if not isinstance(element, int):
                    raise ValueError
                else:
                    self.add(element)

    def parseText(self):
        counter = 0
        while True:
            line = input().split()
            if not line:
                counter += 1
            elif line[0] == "FIM.":
                break
            else:
                # This can be improved by limiting fecthing the node and if it is not available insert it
                for word in line:
                    pword = self.parseWord(word)
                    node = self.get(pword)
                    if node:
                        if counter not in node.lines:
                            node.lines.add(counter)
                    else:
                        self.add(pword, [counter])
                counter += 1

    def parseTextViaFilename(self, filename):
        file = open(filename, "r")
        text = file.readlines()
        counter = 0
        self.head = None
        self.rotations = [0]
        self.total = 0
        self.unique = 0
        for lines in text:
            line = lines.split()
            if not line:
                counter += 1
            elif line[0] == "FIM.":
                break
            else:
                # This can be improved by limiting fecthing the node and if it is not available insert it
                for word in line:
                    self.total += 1
                    pword = self.parseWord(word)
                    node = self.get(pword)
                    if node:
                        if counter not in node.lines:
                            node.lines.add(counter)
                    else:
                        self.unique += 1
                        self.add(pword, [counter])
                counter += 1

    def parseWord(self, word):
        return word.replace(";", "").replace(",", "").replace(".", "").replace("\n", "").replace(")", "").replace(
            "(", "")

    def add(self, node, lines=None):
        new = node if isinstance(node, LinkedNode) else LinkedNode(node, self.substructure(self.substructure))
        if lines:
            for line in lines:
                new.lines.add(line)

        if self.head:
            if new.data < self.head.data:
                new.next = self.head
                self.head = new
            else:
                self.head.add(new)
        else:
            self.head = new

    def get(self, node):
        if self.head:
            new = node if isinstance(node, LinkedNode) else LinkedNode(node)
            return self.head.get(new)
        else:
            return None

    def InOrder(self):
        order = []
        self.head.InOrder(order)
        return ' '.join(map(str, order))


if __name__ == '__main__':
    ll = LinkedList(LinkedList, [2, 6, 4, 5, 3])
    print("test")
