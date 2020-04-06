import random
import timeit
from AVLTree import AVLTree
from RBTree import RBTree
from SplayTree import SplayTree
from BSTree import BinarySearchTree
from LinkedList import LinkedList
import sys


class Tester:
    def __init__(self, items):
        self.items = items

    def test(self, item=None):
        results = []
        if item:
            tests = item
        else:
            tests = self.items
        for element in tests:
            string = input()
            while string != "TCHAU":
                results.append(self.parser(string, element))
                string = input()
            # print(f"Height {avl.root.height()}")
            print('\n'.join(results))

    def timedtest(self, files, item=None):
        tests = item if item else self.items
        for file in files:
            maxlines = len(open(file, "r").readlines()) - 1
            subset50 = self.generateRandomWords(file, 50, 2)
            subset10 = self.generateRandomWords(file, 10)
            avgTime = 0
            for element in tests:
                wrapped = self.wrapper(element.parseTextViaFilename, file)
                buildTime = float(timeit.timeit(wrapped, number=20) * 1000)
                rotates = element.rotations
                buildTime /= 20
                for i in range(50):
                    wrapped = self.wrapper(element.get, subset50[0][i])
                    avgTime += float(timeit.timeit(wrapped, number=20) * 1000)
                lines50 = avgTime / 20
                avgTime = 0
                for i in range(50):
                    wrapped = self.wrapper(self.assocWrapper, element, [subset50[1][i], random.randint(0, maxlines)])
                    avgTime += float(timeit.timeit(wrapped, number=20) * 1000)
                assoc50 = avgTime / 20
                avgTime = 0
                for i in range(500):
                    choice = random.choice(subset10[0])
                    wrapped = self.wrapper(element.get, choice)
                    avgTime += float(timeit.timeit(wrapped, number=20) * 1000)
                lines500 = avgTime / 20

                self.outputData(
                    [file, element.__class__.__name__, element.total, element.unique, rotates, buildTime, lines50,
                     assoc50, lines500])
                avgTime = 0

    def outputData(self, data):
        print(f"Filename : {data[0]}, using {data[1]}")
        print(f"Total number of words: {data[2]}")
        print(f"Total number of unique  words: {data[3]}")
        print(f"Total number of rotations: {data[4]}")
        print(f"Time to build matrix: {data[5]} ms")
        print(f"50 \"LINES\" calls with random words: {data[6]} ms")
        print(f"50 \"ASSOC\" calls with random word and line {data[7]} ms")
        print(f"500 \"LINES\" using a 10 word subset: {data[8]} ms")
        print("----------------END OF REPORT----------------------")

    def parser(self, string, treeType):
        data = string.split()
        if data[0] == "TEXTO":
            treeType.parseText()
            return "GUARDADO."

        if data[0] == "ASSOC":
            node = treeType.get(data[1])
            if node:
                if node.lines.get(int(data[2])):
                    return "ENCONTRADA."
            return "NAO ENCONTRADA."

        if data[0] == "LINHAS":
            node = treeType.get(data[1])
            if node:
                return node.lines.InOrder()
            else:
                return "-1"


    def assocWrapper(self, treeType, data):
        node = treeType.get(data[0])
        if node:
            node.lines.get(int(data[1]))
            return "ENCONTRADA."
        return "NAO ENCONTRADA."

    def generateRandomWords(self, filename, size, iterations=1):
        file = open(filename, "r")
        lines = file.readlines()
        words = [self.parseWord(word) for line in lines for word in line.split()]

        return [random.sample(words, min(size, len(words))) for _ in range(iterations)]

    def parseWord(self, word):
        return word.replace(";", "").replace(",", "").replace(".", "").replace("\n", "").replace(")", "").replace(
            "(", "").replace("\n", "")

    def wrapper(self, func, *args, **kwargs):
        '''
        :param func: function to be passed
        :param args: parameters added to the fucntions
        :param kwargs: keywords added to the function
        :return: function defined as func
        '''

        def wrapped():
            return func(*args, **kwargs)

        return wrapped


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    new = Tester([LinkedList(LinkedList), AVLTree(AVLTree), RBTree(RBTree), SplayTree(SplayTree)])
    #new.timedtest(["Inputs/input2.txt"])
    #new.test()
    new.timedtest(["Inputs/F3TEXTOA.txt", "Inputs/F3TEXTOB.txt", "Inputs/F3TEXTOC.txt", "Inputs/F3TEXTOD.txt"])
    #new.timedtest("Inputs/F3TEXTOD.txt"])
   #new.test()

