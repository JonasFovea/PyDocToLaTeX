import unittest
import os.path
import os
from pyToTeX import *


class MyTestCase(unittest.TestCase):
    def test_convert(self):
        fn = "examplecode.py"
        convert(fn, True)
        self.assertTrue(os.path.isfile("examplecode.tex"))

    def test_cliMissingFileName(self):
        stream = os.popen("python pyToTeX.py")
        out = stream.read().strip()
        self.assertEqual(out,
                         "ERROR: Please provide a path to a .py file, which you want to convert.\n\tAdditional option for overwriting existing .tex files: -o")

    def test_cliTestFalseFileName(self):
        stream = os.popen("python pyToTeX.py testNotFound.py")
        out = stream.read().strip()
        self.assertEqual(out, "ERROR: File or path not found")


if __name__ == '__main__':
    unittest.main()
