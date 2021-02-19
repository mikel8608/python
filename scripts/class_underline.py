'''
  Purpose: Print a line under a string.
  Usage:   var = Line("<char>","<msg>")

  Example: 
    Underline("x","testing")
'''
class Underline():
  def __init__(self,char,msg):
      self.char = char
      self.msg = msg
      print(self.char * len(self.msg))

