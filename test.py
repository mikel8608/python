"""
print('string',5) # , = space so you can place str,int

errors
  exceptions will  run some of the code
  syntax errors will fail to compile so won't run at all
"""

import sys

# Add new path where you have other code
# This is not the preferred version as you need to do this in all scripts.
  #sys.path.append("<add extra paths where you have scripts>")
# Better option is to create a PYTHONPATH variable and asssign the path to this.

"""
 Show all paths used by python.
 List 1st: path where script is running
 List 2nd: paths in the O.S. environment variable
 List 3rd: standard library paths
 List 4th: site packages, 3rd party directories
"""
print(sys.path)


import random

print(random.randrange(1,10))
