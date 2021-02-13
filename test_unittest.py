import unittest

"""
  https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDFTSjFsUlpwUVpCbW9UNHhsbG9scWNGVUtHZ3xBQ3Jtc0tueDFnN2JaUEVuaVk4TFdJd1F5TVk3OV9JTld1RUNBSC1ZTXA0aVI0ZFp1Nk92cm96OHVzYzhKUlg0ZWZBQ01ncm96QklZcGlnUzBlN0hjeTRkc3VJSGFGdm8tQjhtTVRTR1pxbVNFWlNWR0J2V1Y2WQ&q=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funittest.html%23unittest.TestCase.debug
  https://www.youtube.com/watch?v=-nh9rCzPJ20 (1:15min)

  - Using TestCase allows you to setup functions starting with test
  - assert methods are inherited from unittest.
  
  To Test your code
    Either: 
        In vscode, in control pallet search for 'Discover'
      - Then select the pop up to enable framework
      - select framework, then select dir where unit test resides (.root = current dir)
      - select file to test
      - click <run test>
    Or:     In the Termianl window type: python -m unittest <script>
    Or:     You can add the main() fuction call to run from terminal by just calling the script: python test_calc.py

    Then: 
    - Click any of the Icons in bottem left to see errors/info/options
    - Select the Flask Icon in Left Pannel to see info
    
"""

class testcase1(unittest.testcase1):
    def test_add(self):
        result = 10 + 5
        self.assertEqual(result, 1)

    def test_subtract(self):
        result = 10 - 5
        self.assertEqual(result, 5)

#testcase1()

if __name__ == "__main__":
    unittest.main()


