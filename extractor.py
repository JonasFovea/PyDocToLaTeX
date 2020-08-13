def loadFileContent(filename: str):
    content = ""
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError
        pass
    finally:
        pass

    return content

def findFields(fileContent: str):
    lines = fileContent.splitlines()

