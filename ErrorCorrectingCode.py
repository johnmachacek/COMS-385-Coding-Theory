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
      self.code_words = C
      self.__n = m
    else:
      raise ValueError("Error: all code words must have the same length")

  def size(self):
    return len(self.code_words)
  
  def length(self):
    return self.__n
