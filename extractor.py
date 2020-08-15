import re

FIELD_RE = re.compile(r'([a-zA-Z0-9_]*) = .*')
DESCRIPTION_RE = re.compile(r'"""(.*)"""')
FUNCTION_RE = re.compile(r'def ([a-zA-Z_]*)\(([a-zA-Z_,:]*){0,100}\):')


def loadFileContent(filename: str):
    content = ""
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError
    finally:
        pass

    return content


def findFields(fileContent: str):
    lines = fileContent.splitlines()
    fields = []
    for i in range(len(lines) - 1):
        curLine = lines[i]
        nextLine = lines[i + 1]

        matchField = re.search(FIELD_RE, curLine)
        if matchField:
            fieldFound = (matchField.group(1), "")
            matchDescription = re.search(DESCRIPTION_RE, nextLine)
            if matchDescription:
                fieldFound = (matchField.group(1), matchDescription.group(1))
            fields.append(fieldFound)
    if not len(fields):
        return None
    return fields


def findFunctions(fileContent: str):
    lines = fileContent.splitlines()
    functions = []
    for i in range(len(lines) - 1):
        curLine = lines[i]
        nextLine = lines[i + 1]

        matchFunction = re.search(FUNCTION_RE, curLine)
        if matchFunction:
            funcName = matchFunction.group(1)
            funcDescription = re.search(DESCRIPTION_RE, nextLine.strip()).group(1)
            funcParameters = matchFunction.group(2)
            if len(funcParameters):
                funcParameters = funcParameters.split(",")
                for param in funcParameters:
                    param = param.strip()
                    if param.count(" : ") == 1:
                        tempP = param.split(" : ")
                        param = (tempP[0].strip(), tempP[1].strip())
                    else:
                        param = (param, "Any")
            else:
                funcParameters = None

            functions.append((funcName, funcDescription, funcParameters))

    return functions
