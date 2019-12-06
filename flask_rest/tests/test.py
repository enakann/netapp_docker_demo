import unittest
from app2 import Calc


class CalcTest(unittest.TestCase):
     @classmethod
     def setUpClass(cls):
         cls.calc=Calc(1,2)
     def test_add(self):
         self.assertEquals(3,self.calc.add())




if __name__ == "__main__":
    unittest.main()
