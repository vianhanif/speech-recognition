from os import path
import re as regex

class DataSet:
    count_per_line = 10
    FILE = ""
    data_list = []
    separator = ","

    def __init__(self, name="data.txt"):
        self.FILE = name
        self.read()

    def isAWord(self, word):
        return word and word != '\n' and regex.search("|A-Z|a-z|'|", word)

    def write(self, word):
        if self.isAWord(word):
            if not word in self.data_list:
                self.data_list.append(word)

    def save(self):
        self.data_list.sort()
        print("Saving words to " + self.FILE + "...")
        data = open(path.join(path.dirname(path.realpath(__file__)), self.FILE), "w")
        text = ""
        i = 1
        for word in self.data_list:
            if len(self.data_list) <= self.count_per_line:
                text += str(word) + self.separator
                if(i+1 == len(self.data_list)):
                    i = 1
                else:
                    i += 1
            elif i < self.count_per_line:
                text += str(word) + self.separator
                i += 1
            else:
                text += str(word) + self.separator + "\n"
                i = 1
        data.write(text)
        data.close()
        

    def read(self):
        data = open(path.join(path.dirname(path.realpath(__file__)), self.FILE), "r")
        self.data_list = []
        for line in data.readlines():
            i = 0
            words = line.split(self.separator)
            for word in words:
                if self.isAWord(word):
                    self.data_list.append(word)
        data.close()

    def getDataList(self):
        return self.data_list

    def toString(self):
        print("data[" + str(len(self.data_list)) + " words]: " + str(self.data_list))
