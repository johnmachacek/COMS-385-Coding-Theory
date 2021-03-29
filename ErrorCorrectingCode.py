from itertools import combinations

class ErrorCorrectingCode:
    # A class to represent  an error correcting code

    # Attributes
    # ----------
    # code_words: A list of strings representing code words in the code
    # __n: The (common) length of each code word
    # Functions
    # ---------
    # size(): Returns the size of the code (i.e. the number of code words)
    # length(): Returns length of any (all) code word(s)

    def __init__(self, c):

        # Creates an error correcting code.

        # Parameters
        # ----------
        # c: a list of codewords each of which should be string of the same length

        m = len(c[0])
        if all([len(w) == m for w in c]):
            self.__code_words = c
            self.__n = m
        else:
            raise ValueError("all code words must have the same length")

    def size(self):
        return len(self.__code_words)

    def length(self):
        return self.__n

    def getCodeWords(self):
      return (self.__code_words)

    def hammingDist(wrd1, wrd2):
        dist = 0

        length = len(wrd1)
        for i in range(length):
            if wrd1[i] != wrd2[i]:
                dist += 1
        return dist

    def minDistance(self):

        a = self.getCodeWords()

        mindist = []
        for [u, v] in combinations(a, 2):
            mindist.append(ErrorCorrectingCode.hammingDist(u, v))

        return min(mindist)


    def __getitem__(self, i):
        list = self.__code_words
        return list[i]


    def decode(self, codeword):
        closest = []
        dist = self.size()
        wordList = self.getCodeWords()
        #print(wordList)
        numRange = self.length()
        listSize = self.size()

        for i in range(listSize):
            #print(wordList[i], codeword)
            compare = wordList[i]
            if compare == codeword:
                closest.append(compare)

        for word in wordList:
            if (ErrorCorrectingCode.hammingDist(codeword, word) < dist):
                closest.append(word)
                dist = ErrorCorrectingCode.hammingDist(codeword, word)

            elif (ErrorCorrectingCode.hammingDist(codeword, word) == dist):
                    closest.append(word)


        if (len(closest) == 0):
            return
        return closest
