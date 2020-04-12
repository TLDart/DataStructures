from TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self, substructure, root=None):
        """
            Initiates the BSTree
        :param substructure: substructure used in the AVL Tree nodes
        :param root: root of the AVLTree
        """
        self.substructure = substructure
        self.root = None
        self.buildTree(root)
        self.rotations = [0]
        self.unique = 0
        self.total = 0

    def __contains__(self, node):
        """
            Verifies if a node is contained in the tree
        :param node: Node to be searched
        :return: False if not found else True
        """
        new = node if isinstance(node, TreeNode) else TreeNode(node)
        return new in self.root

    def __repr__(self):
        """
            Prints information about the tree
        :return: the tree information
        """
        if not self.root:
            return "No Elements"
        elements = []
        self.root.InOrder(elements)
        return " ".join(list(map(str, elements)))

    def __iadd__(self, node):
        """
            Allows for the tree to add items via += symbol
        :param node: node to be added
        :return: --
        """
        self.add(node)

    def __len__(self):
        """
            Wrapper to use len has the height of the tree
        :return: height of the tree
        """
        return self.root.height()

    def buildTree(self, elements):
        """
            Builds a tree from an array of elements
        :param elements: array of elements to be added
        :return: --
        """
        if elements is None:
            self.root = None
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

    def parseTextViaFilename(self, filename):
        """
            Creates a tree based on the a file
        :param filename: file that will generate the tree
        :return: --
        """
        file = open(filename, "r")
        text = file.readlines()
        counter = 0
        self.root = None
        self.rotations = [0]
        self.unique = 0
        self.total = 0
        for lines in text:
            line = lines.split()
            if not line:
                counter += 1
            elif line[0] == "FIM.":
                break
            else:
                # This can be improved by limiting fetching the node and if it is not available insert it
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
            Adds an element to the tree
        :param node: node to be added (can also add int)
        :param lines: lines to be added corresponding to the node
        :return: --
        """
        new = node if isinstance(node, TreeNode) else TreeNode(node, self.substructure(self.substructure))
        if lines:
            for line in lines:
                new.lines.add(line)

        if self.root:
            self.root = self.root.add(new, self.balancer)
            self.root.red = False
        else:
            self.root = new
            self.root.red = False

    def balancer(self, root, node):
        """
            Balancing function to the bst
        :param root: node being balanced
        :param node: node added (needed to keep track when going up in recursion)
        :return: returns the balanced root
        """
        return root

    def get(self, node):
        """
            Searches for a node in the tree
        :param node: node to be searched
        :return: Node if the node is found, else is None
        """
        if self.root:
            new = node if isinstance(node, TreeNode) else TreeNode(node)
            return self.root.get(new)
        else:
            return None

    def InOrder(self):
        """
            Returns a string representing the tree in order
        :return: string with tree in order
        """
        order = []
        self.root.InOrder(order)
        return ' '.join(map(str, order))

    def PostOrder(self):
        """
            Returns a string representing the tree in PostOrder
        :return: string with tree in order
        """
        order = []
        self.root.PostOrder(order)
        return ' '.join(map(str, order))

    def PreOrder(self):
        """
            Returns a string representing the tree in PreOrder
        :return: string with tree in order
        """
        order = []
        self.root.PreOrder(order)
        return ' '.join(map(str, order))


if __name__ == '__main__':
    bst = BinarySearchTree(BinarySearchTree)
    bst.add(10)
    node = bst.get(10)
    node.lines.add(3)
    print("tegs")
