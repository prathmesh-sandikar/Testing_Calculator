import Calculator

import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        x=10
        y=20
        result=Calculator.add(x,y)
        self.assertEqual(x+y,result)

    def test_sub(self):
        x=20
        y=10
        result=Calculator.sub(x,y)
        self.assertEqual(x-y,result)
if __name__=="__main__":
    unittest.main()
