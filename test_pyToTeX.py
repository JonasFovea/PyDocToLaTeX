import unittest
import os.path
from pyToTeX import *


class MyTestCase(unittest.TestCase):
    def test_convert(self):
        fn = "examplecode.py"
        convert(fn, True)
        self.assertTrue(os.path.isfile("examplecode.tex"))


if __name__ == '__main__':
    unittest.main()
