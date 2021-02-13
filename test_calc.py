import unittest

"""
  https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDFTSjFsUlpwUVpCbW9UNHhsbG9scWNGVUtHZ3xBQ3Jtc0tueDFnN2JaUEVuaVk4TFdJd1F5TVk3OV9JTld1RUNBSC1ZTXA0aVI0ZFp1Nk92cm96OHVzYzhKUlg0ZWZBQ01ncm96QklZcGlnUzBlN0hjeTRkc3VJSGFGdm8tQjhtTVRTR1pxbVNFWlNWR0J2V1Y2WQ&q=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.html%23unittest.TestCase.debug

  Using TestCase allows you to setup functions starting with test
  assert methods rae inherited from unittest.

  To Test your code, in the Termianl window type: python -m unittest <script>
  ...or you can add the main() fuction call to run from terminal by just calling the script: python test_calc.py

  5 // 2.5 = 2 (only returns integer value)
"""


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = 10 + 5
        self.assertEqual(result, 1)

    def test_subtract(self):
        result = 10 - 5
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()

# Show all values stored in memory
dir()
