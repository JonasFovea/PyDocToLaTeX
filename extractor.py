import re

FIELD_RE = re.compile(r'([a-zA-Z0-9_]*) = .*')
DESCRIPTION_RE = re.compile(r'"""(.*)"""')



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
        return  None
    return fields



