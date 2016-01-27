import unittest
from IS105 import add, square

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(add(5,7), 11)

class TestSquare(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_2_2(self):
        self.assertEqual(square(2,2), 4) 

if __name__ == '__main__':
    unittest.main()
