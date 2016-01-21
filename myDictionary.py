class myDictionary(object):
    def __init__(self):
        self.words = list()
    def loadWords(self, file_name):
        f = open(file_name)
        self.words = f.read().splitlines()
    def toLowerCase(self):
        for i in range(0,len(self.words)):
            self.words[i] = self.words[i].lower()
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
    def hasExactWord(self, word):
        if word in self.words:
            return True
        else:
            return False
