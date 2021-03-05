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
        return len(self.code_words)

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