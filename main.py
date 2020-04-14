import random
import timeit
from AVLTree import AVLTree
from RBTree import RBTree
from SplayTree import SplayTree
from BSTree import BinarySearchTree
from LinkedList import LinkedList
from Treap import MaxTreap, MinTreap
import sys
import csv


class Tester:
    def __init__(self, items):
        '''
            Initializes the tester
        :param items: Data Structures to be tested
        '''
        self.items = items

    def test(self, item=None):
        '''
            Runs the test over the Datastructure(s)
        :param item: Optional -> DataStructure can be specified here
        :return: Prints the results of the the test
        '''
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
        '''
            Function used to time test the DataStructures
        :param files: files to test the dataStructures on
        :param item: Optional parameter to test the dataStructures
        :return: --
        '''
        self.rawOutput("raw_output",
                       ["Filename", "TreeType", "Total elements", "Unique Elements", "NUmber of rotations", "Build Time", "50 Lines Assorted",
                        "Assoc 50 Assorted", "Lines 500 10-set"])
        tests = item if item else self.items
        for file in files:
            maxlines = len(open(file, "r").readlines()) - 1
            subset50 = self.generateRandomWords(file, 50, 2)
            subset10 = self.generateRandomWords(file, 10)
            avgTime = 0
            for element in tests:
                wrapped = self.wrapper(element.parseTextViaFilename, file)
                buildTime = float(timeit.timeit(wrapped, number=20) * 1000)
                rotates = element.rotations[0]
                buildTime /= 20
                for i in range(50):
                    if element.__class__.__name__ == "SplayTree":
                        wrapped = self.wrapper(element.find, subset50[0][i])
                        avgTime += float(timeit.timeit(wrapped, number=20) * 1000)
                        element.get(subset50[0][i])
                    else:
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
                    if element.__class__.__name__ == "SplayTree":
                        wrapped = self.wrapper(element.find, choice)
                        avgTime += float(timeit.timeit(wrapped, number=20) * 1000)
                        element.get(choice)
                    else:
                        wrapped = self.wrapper(element.get, choice)
                        avgTime += float(timeit.timeit(wrapped, number=20) * 1000)
                lines500 = avgTime / 20

                self.rawOutput("raw_output", [file, element.__class__.__name__, element.total, element.unique, rotates, buildTime, lines50,
                     assoc50, lines500])
                self.outputData(
                    [file, element.__class__.__name__, element.total, element.unique, rotates, buildTime, lines50,
                     assoc50, lines500])
                avgTime = 0

    def rawOutput(self, filename, data):
        with open(f'{filename}.csv', mode='a') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(data)

    def outputData(self, data):
        '''
        Formats the data a report can be printed
        :param data: array that contains all time data about a dataStructure
        :return: --
        '''
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
        '''
            Function that receives a string and activates the correct function based on that
        :param string: string to be evaluated
        :param treeType: type of tree being currently used
        :return: result of an operation over the string
        '''
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
        '''
            Wrapper required to use the timeit function
        :param treeType: Tree used for testing
        :param data: array that contains both word and line to be found
        :return:
        '''
        node = treeType.get(data[0])
        if node:
            node.lines.get(int(data[1]))
            return "ENCONTRADA."
        return "NAO ENCONTRADA."

    def generateRandomWords(self, filename, size, iterations=1):
        '''
            Generates a set random words from a filename
        :param filename: The source of the words
        :param size: numbers of words to be generated
        :param iterations: number of sets of words to be generated
        :return:
        '''
        file = open(filename, "r")
        lines = file.readlines()
        words = [self.parseWord(word) for line in lines for word in line.split()]

        return [random.sample(words, min(size, len(words))) for _ in range(iterations)]

    def parseWord(self, word):
        '''
            Removes all extra characters from a word
        :param word: Word to be parsed
        :return: word parsed
        '''
        return word.replace(";", "").replace(",", "").replace(".", "").replace("\n", "").replace(")", "").replace(
            "(", "").replace("\n", "")

    def wrapper(self, func, *args, **kwargs):
        '''
        :param func: function to be passed
        :param args: parameters added to the functions
        :param kwargs: keywords added to the function
        :return: function defined as func
        '''

        def wrapped():
            return func(*args, **kwargs)

        return wrapped


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    new = Tester([SplayTree(SplayTree)])
    #new.timedtest(["Inputs/input2.txt"])
    #new.test()
    #new.timedtest(["Inputs/input3.txt"])
    new.timedtest(["Inputs/F3TEXTOA.txt","Inputs/F3TEXTOB.txt","Inputs/F3TEXTOC.txt","Inputs/F3TEXTOD.txt"])
   #new.test()

