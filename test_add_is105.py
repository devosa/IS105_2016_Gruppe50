import unittest
from IS105 import add, divide

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(add(5,7), 11)
        
class TestDivide(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_20_10(self):
        self.assertEqual(divide(20,10), 2)
        
if __name__ == '__main__':
    unittest.main()
    