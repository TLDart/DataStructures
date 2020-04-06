from TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self, substructure, root=None):
        self.substructure = substructure
        self.root = None
        self.buildTree(root)
        self.rotations = [0]
        self.unique = 0
        self.total = 0

    def __contains__(self, node):
        new = node if isinstance(node, TreeNode) else TreeNode(node)
        return new in self.root

    def __repr__(self):
        if not self.root:
            return "No Elements"
        elements = []
        self.root.InOrder(elements)
        return " ".join(list(map(str, elements)))

    def __iadd__(self, node):
        self.add(node)

    def __len__(self):
        return self.root.height()

    def buildTree(self, elements):
        if elements is None:
            self.root = None
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
        return root

    def get(self, node):
        if self.root:
            new = node if isinstance(node, TreeNode) else TreeNode(node)
            return self.root.get(new)
        else:
            return None

    def InOrder(self):
        order = []
        self.root.InOrder(order)
        return ' '.join(map(str, order))

    def PostOrder(self):
        order = []
        self.root.PostOrder(order)
        return ' '.join(map(str, order))

    def PreOrder(self):
        order = []
        self.root.PreOrder(order)
        return ' '.join(map(str, order))


if __name__ == '__main__':
    bst = BinarySearchTree(BinarySearchTree)
    bst.add(10)
    node = bst.get(10)
    node.lines.add(3)
    print("tegs")
