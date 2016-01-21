class myDictionary(object):
    def __init__(self):
        self.words = list()
    def loadWords(self, file_name):
        f = open(file_name)
        self.words = f.read().splitlines()
    def hasWord(self, word):
        s = str(word)
        if s in self.words:
            return True
        elif s.upper() in self.words:
            return True
        elif s.lower() in self.words:
            return True
        else:
            return False
    


myDict = myDictionary()
file_name = 'C:\\Python34\\words'
try:
    myDict.loadWords(file_name)
except FileNotFoundError:
    print('Couldn\'t load the file ', file_name)
else:
    inputWord = input('I speak english.  Give me a word, and I\'ll tell you if it\'s real\n')
    print(myDict.hasWord(inputWord))
