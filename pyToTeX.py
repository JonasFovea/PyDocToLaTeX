import os
import sys

from docBuilder import *
from extractor import *

FILENAME_RE = re.compile(r'(\w+)\.py$')
PATH_RE = re.compile(r'(.*)?(\w+)\.py$')
OVERRIDE_OPTION_RE = re.compile(r'-o$')


def convert(fileName: str, override=False):
    name = re.search(FILENAME_RE, fileName).group(1)
    texName = name + ".tex"
    if os.path.isfile(texName):
        if os.stat(texName) != 0 and not override:
            raise Exception("File already exists")

    with open(fileName, 'r') as sourceFile:
        content = sourceFile.read()
        doc = Doc(name)

        fields = findFields(content)
        for pyField in fields:
            texField = Field(pyField[0])
            texField.setDescription(pyField[1])
            doc.addField(texField)

        functions = findFunctions(content)
        for pyFunction in functions:
            texFunction = Function(pyFunction[0])
            texFunction.setDescription(pyFunction[1])
            if pyFunction[2]:
                for param in pyFunction[2]:
                    texParam = Parameter(param[0])
                    texParam.setType(param[1])
                    texFunction.addParameter(texParam)
            doc.addFunction(texFunction)

        classes = findClasses(content)
        for pyClass in classes:
            texClass = Class(pyClass[0])
            texClass.setDescription(pyClass[1])
            for pyField in pyClass[2]:
                texField = Field(pyField[0])
                texField.setDescription(pyField[1])
                texClass.addField(texField)

            for pyFunction in pyClass[3]:
                texFunction = Function(pyFunction[0])
                texFunction.setDescription(pyFunction[1])
                for pyParam in pyFunction[2]:
                    texParam = Parameter(pyParam[0])
                    texParam.setType(pyParam[1])
                    texFunction.addParameter(texParam)
                texClass.addFunction(texFunction)
            doc.addClass(texClass)

        doc.exportFile(texName)


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 1:
        print(
            "\tERROR: Please provide a path to a .py file, which you want to convert.\nAdditional option for overwriting existing .tex files: -o")
    elif len(argv) == 2:
        if re.search(PATH_RE, argv[1].strip()):
            try:
                convert(argv[1].strip())
                nameMatch = re.search(PATH_RE, argv[1].strip())
                print("\tSUCCESS: Converted " + nameMatch.group(1) + nameMatch.group(2) + ".py into " + nameMatch.group(
                    1) + nameMatch.group(2) + ".tex")
            except Exception as e:
                print("\tERROR: " + str(e))
        else:
            print("\tERROR: Please provide a valid filepath.")
    elif len(argv) == 3:
        if re.search(PATH_RE, argv[1].strip()) and re.search(OVERRIDE_OPTION_RE, argv[2].strip()):
            try:
                convert(argv[1].strip(), True)
                nameMatch = re.search(PATH_RE, argv[1].strip())
                print("\tSUCCESS: Converted " + nameMatch.group(1) + nameMatch.group(2) + ".py into " + nameMatch.group(
                    1) + nameMatch.group(2) + ".tex")
            except Exception as e:
                print("\tERROR: " + str(e))
        else:
            print("\tERROR: Please provide valid arguments.\nAdditional option for overwriting existing .tex files: -o")
    else:
        print("\tERROR: Please provide valid arguments.\nAdditional option for overwriting existing .tex files: -o")
