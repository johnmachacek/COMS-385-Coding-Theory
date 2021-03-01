#imports
from itertools import combinations

class ErrorCorrectingCode:
  '''
  A class to represent  an error correcting code

  Attributes
  ----------
  code_words: A list of strings representing code words in the code
  __n: The (common) length of each code word

  Functions
  ---------
  size(): Returns the size of the code (i.e. the number of code words)
  length(): Returns length of any (all) code word(s)
  '''

  def __init__(self, C):
    '''
    Creates an error correcting code.

    Parameters
    ----------
    C: a list of codewords each of which should be string of the same length
    '''
    m = len(C[0])
    if all([len(w) == m for w in C]):
      self.__code_words = C
      self.__n = m
    else:
      raise ValueError("All code words must have the same length")

  def size(self):
    return len(self.code_words)

  def length(self):
    return self.__n


#Hamming distance function that takes two words as parameters
  def hammingDist(wrd1, wrd2):
    dist = 0
    length = len(wrd1)
    for i in range(length):
        if wrd1[i] != wrd2[i]:
            dist += 1
    return dist


#A function to get code words (Returns codeWords in a LIST)
  def getCodeWords(self):
    return(self.__code_words)


#A function to create the replication code for a user specified length
  def repititionCode(length):
    #create the 0 replication of size length
    string0 = "".join('0' for i in range(length))

    #create the 1 replication of size length
    string1 = "".join('1' for i in range(length))

    repitition = [string0, string1]
    return repitition


#A function that will get a subscripted item from the list of code words (ex. code[i])
  def __getitem__(self, i):
    list = self.__code_words
    return list[i]
