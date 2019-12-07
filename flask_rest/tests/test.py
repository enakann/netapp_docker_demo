import unittest
from app2 import Calc


class CalcTest(unittest.TestCase):
     @classmethod
     def setUpClass(cls):
         cls.calc=Calc(1,2)
     def test_add(self):
         self.assertEqual(3,self.calc.add())
     def test_add1(self):
         self.assertEqual(2,self.calc.add())



if __name__ == "__main__":
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_reports'))
