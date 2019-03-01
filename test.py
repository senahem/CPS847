import unittest

class ForVideo(unittest.TestCase):
    def setUp(self):
        print 'some test'

    def test_search_in_python_org(self):
        print 'something'

    def tearDown(self):
        print 'something'

if __name__ == "__main__":
    unittest.main()
