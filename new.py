import unittest
import function

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(function.cps3619(4), 16)

if __name__ == '__main__':
    unittest.main()
