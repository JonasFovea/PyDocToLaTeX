import unittest
from extractor import *


class MyTestCase(unittest.TestCase):
    def test_loadFileContent(self):
        fn = "examplecode.py"
        cont = loadFileContent(fn)
        f = open(fn)
        fileCont = f.read()
        f.close()
        self.assertEqual(cont, fileCont)
        self.assertRaises(FileNotFoundError, loadFileContent, "")

    def test_findFields(self):
        fn = "examplecode.py"
        cont = loadFileContent(fn)
        self.assertEqual(findFields(cont), [("a", "a is a variable"), ("varB", "varB is another variable"), ("V_ariable_C", "")])


if __name__ == '__main__':
    unittest.main()
