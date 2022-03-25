import Calculator

import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.x=34
        self.y=30

    def tearDown(self):
        self.x=0
        self.y=0


    def test_add(self):
        # x=10
        # y=20
        result=Calculator.add(self.x,self.y)
        self.assertEqual(self.x+self.y,result)



    def test_sub(self):
        #ARRANGE
        # x=20
        # y=10
        #ACT
        result=Calculator.sub(self.x,self.y)
        #ASSERT
        self.assertEqual(self.x-self.y,result)

    def test_mult(self):
        # x=5
        # y=5
        result=Calculator.mult(self.x,self.y)
        self.assertEqual(self.x*self.y,result)

    def test_div(self):
        # x=10
        # y=2
        result=Calculator.div(self.x,self.y)
        self.assertEqual(self.x/self.y,result)
if __name__=="__main__":
    unittest.main()
