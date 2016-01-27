import unittest
from IS105 import add, remain

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(add(5,7), 11)

class TestRemain(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_4_3(self):
        self.assertEqual(remain(4,3), 1)

if __name__ == '__main__':
    unittest.main()
