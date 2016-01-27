import unittest
from IS105 import add, sub, multiply


class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(add(5,7), 12)

class TestSub(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_10_2(self):
        self.assertEqual(sub(10,2), 8)
        
class TestMultiply(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(multiply(2,10), 20)

if __name__ == '__main__':
    unittest.main()
