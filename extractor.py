import re

FIELD_RE = re.compile(r'^([a-zA-Z0-9_]*) = .*')
DESCRIPTION_RE = re.compile(r'"""(.*)"""')
FUNCTION_RE = re.compile(r'^def (\w+)\((.*)\):')
CLASS_RE = re.compile(r'^class (\w+):')


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
            funcDescription = re.search(DESCRIPTION_RE, nextLine.rstrip()).group(1)
            funcParameters = matchFunction.group(2)
            paramList = []
            if len(funcParameters) > 0:
                for p in funcParameters.strip().split(","):
                    tmpP = p.strip().split(":")
                    if len(tmpP) == 2:
                        paramList.append((tmpP[0].strip(), tmpP[1].strip()))
                    else:
                        paramList.append((tmpP[0].strip(), "Any"))
            else:
                paramList = None

            functions.append((funcName, funcDescription, paramList))

    return functions


def findClasses(fileContent: str):
    lines = fileContent.splitlines()
    classes = []
    classList = []
    for i in range(len(lines)-1):
        curLine = lines[i]
        matchClass = re.search(CLASS_RE, curLine)
        if matchClass:
            classList.append(i)

    for x in range(len(classList)):
        cName = re.search(CLASS_RE, lines[classList[x]]).group(1)
        cDescription = re.search(DESCRIPTION_RE, lines[classList[x]+1]).group(1)
        start = classList[x]+1
        if x < len(classList)-1:
            end = classList[x+1]-1
        else:
            end = len(lines)-1

        cBody = []
        for line in lines[start:end]:
            cBody.append(line.replace("    ", "", 1))

        bodyString = "\n".join(cBody)

        cFields = findFields(bodyString)
        cFunctions = findFunctions(bodyString)
        classes.append((cName, cDescription, cFields, cFunctions))

    return  classes

