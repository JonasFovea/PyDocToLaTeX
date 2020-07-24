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
        tFunc1 = Function()
        tFunc2 = Function("Function2")

    def test_createField(self):
        tField1 = Field()
        tField2 = Field("TestField2")

    def test_addClass(self):
        tDoc = Doc()
        tDoc.addClass(Class("Test1"))
        tDoc.addClass(Class("Test2"))

    def test_DocGetName(self):
        tDoc1 = Doc("TestName")
        self.assertEqual(tDoc1.getName(), "TestName")
        tDoc2 = Doc("TestNameABC")
        self.assertEqual(tDoc2.getName(), "TestNameABC")

    def test_ClassGetName(self):
        tClass1 = Class("TestName")
        self.assertEqual(tClass1.getName(), "TestName")
        tClass2 = Class("TestNameABC")
        self.assertEqual(tClass2.getName(), "TestNameABC")

    def test_DocGetClasses(self):
        tDoc = Doc("Documentation")
        tC1 = Class("Class1")
        tC2 = Class("Class2")
        tDoc.addClass(tC1)
        tDoc.addClass(tC2)
        self.assertListEqual(tDoc.getClasses(), [tC1, tC2])

    def test_DocAddFunction(self):
        tDoc = Doc("Documentation")
        tFunction1 = Function()
        tFunction2 = Function("Function2")
        tDoc.addFunction(tFunction1)
        tDoc.addFunction(tFunction2)

    def test_DocGetFunctions(self):
        tDoc = Doc("Documentation")
        tFunction1 = Function()
        tFunction2 = Function("Function2")
        tDoc.addFunction(tFunction1)
        tDoc.addFunction(tFunction2)
        self.assertListEqual(tDoc.getFunctions(), [tFunction1, tFunction2])


if __name__ == '__main__':
    unittest.main()
