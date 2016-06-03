import unittest
from IS105 import add, sub, multiply, remain, square, divide


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

class TestRemain(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_4_3(self):
        self.assertEqual(remain(4,3), 1)

class TestSquare(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_2_2(self):
        self.assertEqual(square(2,2), 4) 
        
class TestDivide(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_20_10(self):
        self.assertEqual(divide(20,10), 2)

if __name__ == '__main__':
    unittest.main()
