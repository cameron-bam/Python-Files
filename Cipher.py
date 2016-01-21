import string
class Cipher(object):
    def __init__(self, keystring, lookupLetters):
        self.key = {key:letter for key,letter in zip(keystring,lookupLetters)}
    def decrypt(self, text):
        newText = str()
        for i in range (0,len(text)):
            if text[i] in (string.ascii_letters):
                newText += self.key[text[i]]
            else:
                newText += text[i]
        return newText
