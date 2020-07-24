class Doc:
    name = ""
    classes = []
    functions = []

    def __init__(self, name=None):
        self.name = name

    def getName(self):
        return self.name

    def addClass(self, argClass):
        self.classes.append(argClass)

    def getClasses(self):
        return self.classes

    def addFunction(self, func):
        self.functions.append(func)

    def getFunctions(self):
        return self.functions

class Class:
    name = ""
    def __init__(self, name=None):
        self.name = name

    def getName(self):
        return self.name


class Function:
    name = ""
    def __init__(self, name=None):
        self.name = name


class Field:
    def __init__(self, name=None):
        pass
