import unittest
from docBuilder import *


class MyTestCase(unittest.TestCase):
    def test_createDoc(self):
        tDoc1 = Doc()
        tDoc2 = Doc("TestDoc2")

    def test_createClass(self):
        tClass1 = Class()
        tClass2 = Class("TestClass2")

    def test_createFunction(self):
        tFunc = Function()

    def test_createField(self):
        tField1 = Field()
        tField2 = Field("TestField2")

    def test_addClass(self):
        tDoc = Doc()
        tDoc.addClass("Test1")

    def test_DocGetName(self):
        tDoc1 = Doc("TestName")
        self.assertEqual(tDoc1.getName(), "TestName")
        tDoc2 = Doc("TestNameABC")
        self.assertEqual(tDoc2.getName(), "TestNameABC")


if __name__ == '__main__':
    unittest.main()
