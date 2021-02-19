'''
  Purpose: Print an Underline using a character and message as input
  Usage:   line("<char>","<msg>")

  Example:
    line("#","Place a line beneth this sentence")
'''
def line(char="-",msg=None):
  print(char * len(msg))
