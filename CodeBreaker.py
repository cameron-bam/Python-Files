import profile
import Cipher
import sys

def recursiveSolution(remaining_chars, chars_to_match, cipher, dictionary, encrypted_text, checked_results):
    if len(remaining_chars) == 1:
        remaining_char = remaining_chars[0]
        for letter in (chars_to_match):
            cipher.updateKey(remaining_char, letter)
            if cipher.decrypt(encrypted_text) in dictionary:
                return cipher, cipher.decrypt(encrypted_text)
        cipher.updateKey(remaining_char, chars_to_match[0])
        return cipher, -1, len(chars_to_match) + checked_results
    
    current_char = remaining_chars[len(remaining_chars)-1]
    for letter in (chars_to_match):
        cipher.updateKey(current_char, letter)
        results = recursiveSolution(remaining_chars[0:-1], chars_to_match, cipher, dictionary, encrypted_text, checked_results)
        if results[1] != -1:
            return results
        checked_results = results[2]
    if len(remaining_chars) == 3:
        print((checked_results/(len(chars_to_match)**len(cipher.key.keys())))*100,'% done...')
    cipher.updateKey(current_char, chars_to_match[0])
    return cipher, -1, checked_results

def createCiphers(keyLetters, lookupLetters, encryptedWords, dictionary):
    l = len(keyLetters)
    index = -1
    cipherList = (list(), list())
    for i in range(0,l):
        if len(lookupLetters[i]) != 1:
            index = i
            break
    if index != -1:
        lookupLettersNew = list(lookupLetters)
        for i in range(0,len(lookupLetters[index])):
            lookupLettersNew[index] = lookupLetters[index][i]
            solutions = createCiphers(keyLetters, lookupLettersNew, encryptedWords, dictionary)
            for sol in range(0,len(solutions[0])):
                cipherList[0].append(solutions[0][sol])
                cipherList[1].append(solutions[1][sol])
        return cipherList
    else:
        newCipher = Cipher.Cipher(keyLetters, lookupLetters)
        if newCipher.decrypt(encryptedWords[0]) in dictionary:
            isSolution = True
            decryptedWords = list()
            for word in range(0,len(encryptedWords)):
                decryptedWords.append(newCipher.decrypt(encryptedWords[word]))
                if newCipher.decrypt(encryptedWords[word]) not in dictionary:
                    isSolution = False
                    break
            if isSolution == True:
                cipherList[0].append(newCipher)
                cipherList[1].append(decryptedWords)
        return cipherList
        

def main():
    import string
    file = open('C:\\Python34\\words')
    words = file.read().splitlines()
    wordDict = {x.lower():1 for x in words}
    encryptedText = input('Give me text to decrypt\n')
    encryptedWords = encryptedText.split()
    keyLetters = set(encryptedText)
    keyLetters.remove(' ')
    print(keyLetters)
    lookupLetters = list()
    for i in range(0,len(keyLetters)):
        lookupLetters.append(string.ascii_lowercase)
    print('Building solutions...')
    cipherList = createCiphers(keyLetters, lookupLetters, encryptedWords, wordDict)    
    for sol in range(0, len(cipherList[0])):
        print('Solution #', sol)
        print('Decrypted text:', cipherList[1][sol])
        print('Cipher:', cipherList[0][sol].key)
    del cipherList
    sys.exit(0)
main()
