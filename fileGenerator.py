from random import random, randrange

myAlphabet = ["a","b","c"]


def generateWord(size, alphabet):
    word = []
    for i in range(0, size):
        word.append(alphabet[int(random() * len(alphabet))])
    return ''.join(word)


def fileGenerator(split, n, alphabet, minSize, maxSize):
    for i in range(0, split):
        file = open("./data/file_" + str(i) + ".txt", "a")
        wordList = []
        for j in range(0, n):
            wordSize = randrange(minSize, maxSize + 1)
            word = generateWord(wordSize, alphabet)
            wordList.append(word)
            
        text = '\n'.join(wordList)
        file.write(text)
        file.close()
        
fileGenerator(4, 100, myAlphabet, 2, 5)