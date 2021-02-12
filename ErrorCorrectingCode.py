class ErrorCorrectingCode:
  '''This class defines an error correcting code'''
  
  def __init__(self, C):
    self.code_words = C
  
  def size(self):
    return len(C)
  
  def length(self):
    return len(C[0])
