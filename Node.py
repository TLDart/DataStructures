class Node:
    def __init__(self, data=None, lines=None):
        self.lines = [] if lines is None else lines
        self.data = data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data <= other.data

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __repr__(self):
        return str(self.data)
