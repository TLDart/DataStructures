class Node:
    def __init__(self, data=None, lines=None):
        self.lines = [] if lines is None else lines
        self.data = data

    def __gt__(self, other):
        '''
            Replaces the > function so that calling self.data is no longer required
        :param other: node to be compared with
        :return: result of the comparison
        '''
        return self.data > other.data

    def __ge__(self, other):
        '''
            Replaces the >= function so that calling self.data is no longer required
        :param other: node to be compared with
        :return: result of the comparison
        '''
        return self.data >= other.data

    def __lt__(self, other):
        '''
            Replaces the < function so that calling self.data is no longer required
        :param other: node to be compared with
        :return: result of the comparison
        '''
        return self.data < other.data

    def __le__(self, other):
        '''
            Replaces the <= function so that calling self.data is no longer required
        :param other: node to be compared with
        :return: result of the comparison
        '''
        return self.data <= other.data

    def __eq__(self, other):
        '''
            Replaces the == function so that calling self.data is no longer required
        :param other: node to be compared with
        :return: result of the comparison
        '''
        return self.data == other.data

    def __ne__(self, other):
        '''
            Replaces the != function so that calling self.data is no longer required
        :param other: node to be compared with
        :return: result of the comparison
        '''
        return self.data != other.data

    def __repr__(self):
        '''
            Makes it so the print function prints the value of the node
        :return: data of the node
        '''
        return str(self.data)
