from LinkedNode import LinkedNode


class LinkedList:
    def __init__(self, substructure, head=None):
        """
            Initiates the LinkedList
        :param substructure: substructure used in the LinkedList nodes
        :param root: root of the LinkedList
        """
        self.head = None
        self.substructure = substructure
        self.buildTree(head)
        self.rotations = [0]
        self.total = 0
        self.unique = 0

    def __repr__(self):
        """
            Allows for printing to print the linked list in order
        :return: --
        """
        return self.InOrder()

    def __contains__(self, node):
        """
            Searches the linked lists
        :param node: node to the searched
        :return: True if found, False if not found
        """
        new = node if isinstance(node, LinkedNode) else LinkedNode(node)
        return new in self.head

    def buildTree(self, elements):
        """
            Builds a tree from an array of elements
        :param elements: array of elements to be added
        :return: --
        """
        if elements is None:
            self.head = None
        else:
            for element in elements:
                if not isinstance(element, int):
                    raise ValueError
                else:
                    self.add(element)

    def parseText(self):
        """
            Generates a tree base on input
        :return: --
        """
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
        """
            Creates a tree based on the a file
        :param filename: file that will generate the tree
        :return: --
        """
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
        """
           Remove unwanted characters from a string
       :param word: Word to be parsed
       :return: Parsed worse
       """
        return word.replace(";", "").replace(",", "").replace(".", "").replace("\n", "").replace(")", "").replace(
            "(", "")

    def add(self, node, lines=None):
        """
            Adds an element to the Linked List
        :param node: node to be added (can also add int)
        :param lines: lines to be added corresponding to the node
        :return: --
        """
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
        """
            Searches for a node in the Linked List
        :param node: node to be searched
        :return: Node if the node is found, else is None
        """
        if self.head:
            new = node if isinstance(node, LinkedNode) else LinkedNode(node)
            return self.head.get(new)
        else:
            return None

    def InOrder(self):
        """
            Returns a string representing the tree in order
        :return: string with tree in order
        """
        order = []
        self.head.InOrder(order)
        return ' '.join(map(str, order))


if __name__ == '__main__':
    ll = LinkedList(LinkedList, [2, 6, 4, 5, 3])
    print("test")
