"""
  If you created vars using _ as the prefix you will need to specify those also.
  This code is defensive so you don't remove vars like __name__ etc...
"""

for name in dir():
    if not name.startswith("_"):
        del globals()[name]

for name in dir():
    if not name.startswith("_"):
        del locals()[name]