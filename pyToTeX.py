import re
import os
from extractor import *
from docBuilder import *

FILENAME_RE = re.compile(r'(\w+)\.py')


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