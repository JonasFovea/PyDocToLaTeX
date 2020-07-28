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

    def test_CreateParameter(self):
        tParam1 = Parameter()
        tParam2 = Parameter("Parameter2")

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

    def test_FunctionGetName(self):
        tFunc1 = Function()
        self.assertEqual(tFunc1.getName(), "")
        tFunc2 = Function("Function2")
        self.assertEqual(tFunc2.getName(), "Function2")

    def test_FieldGetName(self):
        tField1 = Field()
        self.assertEqual(tField1.getName(), "")
        tField2 = Field("Field2")
        self.assertEqual(tField2.getName(), "Field2")

    def test_ParameterGetName(self):
        tParam1 = Parameter()
        self.assertEqual(tParam1.getName(), "")
        tParam2 = Parameter("Parameter2")
        self.assertEqual(tParam2.getName(), "Parameter2")

    def test_DocSetDescription(self):
        tDoc = Doc("Documentation")
        tDoc.setDescription("This is the description of the Documentation.")

    def test_DocGetDescription(self):
        tDoc = Doc("Documentation")
        tDoc.setDescription("This is the description of the Documentation.")
        self.assertEqual(tDoc.getDescription(), "This is the description of the Documentation.")

    def test_DocAddClass(self):
        tDoc = Doc()
        tDoc.addClass(Class("Test1"))
        tDoc.addClass(Class("Test2"))

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

    def test_DocAddField(self):
        tDoc = Doc("Dokumentation")
        tF1 = Field()
        tF2 = Field("Field2")
        tDoc.addField(tF1)
        tDoc.addField(tF2)

    def test_DocGetFields(self):
        tDoc = Doc("Dokumentation")
        tF1 = Field()
        tF2 = Field("Field2")
        tDoc.addField(tF1)
        tDoc.addField(tF2)
        self.assertListEqual(tDoc.getFields(), [tF1, tF2])

    def test_ClassAddFunction(self):
        tClass = Class("Test Class")
        tFunc1 = Function("Function1")
        tFunc2 = Function("Function2")
        tClass.addFunction(tFunc1)
        tClass.addFunction(tFunc2)

    def test_ClassGetFunctions(self):
        tClass = Class("Test Class")
        tFunc1 = Function("Function1")
        tFunc2 = Function("Function2")
        tClass.addFunction(tFunc1)
        tClass.addFunction(tFunc2)
        self.assertListEqual(tClass.getFunctions(), [tFunc1, tFunc2])

    def test_ClassAddField(self):
        tClass = Class("Test Class")
        tField1 = Field("Field1")
        tField2 = Field("Field2")
        tClass.addField(tField1)
        tClass.addField(tField2)

    def test_ClassGetFields(self):
        tClass = Class("Test Class")
        tField1 = Field("Field1")
        tField2 = Field("Field2")
        tClass.addField(tField1)
        tClass.addField(tField2)
        self.assertListEqual(tClass.getFields(), [tField1, tField2])

    def test_ParameterSetDescription(self):
        tParam = Parameter("x")
        tParam.setDescription("x-Coordinate")

    def test_ParameterGetDescription(self):
        tParam = Parameter("x")
        tParam.setDescription("x-Coordinate")
        self.assertEqual(tParam.getDescription(), "x-Coordinate")

    def test_ParameterSetType(self):
        tParam = Parameter("Test Parameter")
        tParam.setType("int")

    def test_ParameterGetType(self):
        tParam = Parameter("Test Parameter")
        tParam.setType("int")
        self.assertEqual(tParam.getType(), "int")

    def test_FunctionSetDescription(self):
        tFunc = Function("Test Function")
        tFunc.setDescription("Function returns the Sum of the Parameters a and b.")

    def test_FunctionGetDescription(self):
        tFunc = Function("Test Function")
        tFunc.setDescription("Function returns the Sum of the Parameters a and b.")
        self.assertEqual(tFunc.getDescription(), "Function returns the Sum of the Parameters a and b.")

    def test_FunctionAddParameter(self):
        tFunc = Function()
        tParam1 = Parameter("Param 1")
        tParam2 = Parameter("Parameter 2")
        tFunc.addParameter(tParam1)
        tFunc.addParameter(tParam2)

    def test_FunctionGetParameters(self):
        tFunc = Function()
        tParam1 = Parameter("Param 1")
        tParam2 = Parameter("Parameter 2")
        tFunc.addParameter(tParam1)
        tFunc.addParameter(tParam2)
        self.assertListEqual(tFunc.getParameters(), [tParam1, tParam2])

    def test_ClassSetDescription(self):
        tClass = Class()
        tClass.setDescription("Lorem ipsum dolor sit amet")

    def test_ClassGetDescription(self):
        tClass = Class()
        tClass.setDescription("Lorem ipsum dolor sit amet")
        self.assertEqual(tClass.getDescription(), "Lorem ipsum dolor sit amet")

    def test_FieldSetType(self):
        tField = Field("Test Field")
        tField.setType("int")

    def test_FieldGetType(self):
        tField = Field("Test Field")
        tField.setType("int")
        self.assertEqual(tField.getType(), "int")

    def test_FieldSetDescription(self):
        tField = Field()
        tField.setDescription("Description")

    def test_FieldGetDescription(self):
        tField = Field()
        tField.setDescription("Description")
        self.assertEqual(tField.getDescription(), "Description")

    # ===========Doc build tests===========
    def test_DocBuildFrame(self):
        tDoc1 = Doc("main.py")
        self.assertEqual(tDoc1.buildFrame(), "\section{main.py}\n")
        tDoc2 = Doc("descriptiontest.py")
        tDoc2.setDescription("Description text at the top of the file.")
        self.assertEqual(tDoc2.buildFrame(), "\section{descriptiontest.py}\nDescription text at the top of the file.\n")

    def test_DocBuildFields(self):
        tDoc = Doc("main.py")
        tField = Field("x")
        tField.setType("int")
        tField.setDescription("Field stores the variable named x")
        tDoc.addField(tField)
        self.assertEqual(tDoc.buildFields(),
                         "\subsection{Fields}\n\\begin{tabular}{|l|l|l|}\hline\n\t\\textbf{name} & \\textbf{type} & \\textbf{description}\\\\\\hline\n\tx & int & Field stores the variable named x \\\\\\hline\n\end{tabular}\n")

    def test_DocExportFile(self):
        tDoc = Doc("main.py")
        tField = Field("x")
        tField.setType("int")
        tField.setDescription("Field stores the variable named x")
        tDoc.addField(tField)
        filename = "testfile.tex"
        tDoc.exportFile(filename)

    def test_DocBuildClasses(self):
        tDoc = Doc("main.py")
        tClass = Class("Testclass")
        tField = Field("Class Test Field")
        tField.setType("str")
        tField.setDescription("Field of a class in the documentation")
        tClass.addField(tField)
        tFunc = Function("testFunc")
        tFunc.setDescription("Function which processes x")
        tParam = Parameter("x")
        tParam.setType("int")
        tParam.setDescription("Variable x")
        tFunc.addParameter(tParam)
        tClass.addFunction(tFunc)
        tDoc.addClass(tClass)

        self.assertEqual(tDoc.buildClasses(), "\\subsection{Classes}\n\\subsubsection{Testclass}\n\\textbf{Fields}\\\\[0.5\\baselineskip]\n\\begin{tabular}{|p{0.4\\linewidth}|p{0.1\\linewidth}|p{0.5\\linewidth}|}\\hline\n\\textbf{name} & \\textbf{type} & \\textbf{description}\\\\\\hline\nClass Test Field & str & Field of a class in the documentation\\\\\\hline\n\\end{tabular}\\\\[\\baselineskip]\n\\textbf{Functions}\\\\[0.5\\baselineskip]\n\\begin{tabular}{|p{0.15\\linewidth}|p{0.35\\linewidth}|p{0.5\\linewidth}|}\\hline\n\\textbf{name} & \\textbf{parameters} & \\textbf{description}\\\\\\hline\ntestFunc & \\begin{minipage}{\\textwidth}\\begin{itemize}\\item int x :: Variable x \\end{itemize}\\end{minipage} & Function which processes x\\\\\\hline\n\\end{tabular}\\\\\n")

if __name__ == '__main__':
    unittest.main()
