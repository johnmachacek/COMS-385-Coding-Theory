class ErrorCorrectingCode:
  '''This class define an error correcting code'''
  
  def __init__(self, C):
    self.code_words = C
  
  def size(self):
    return len(C)
