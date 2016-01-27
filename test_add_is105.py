import unittest
from IS105 import add, sub

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(add(5,7), 11)

class TestSub(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_10_2(self):
        self.assertEqual(sub,10,2), 8)

if __name__ == '__main__':
    unittest.main()
