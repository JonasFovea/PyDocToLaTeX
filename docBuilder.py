class Doc:
    name = ""
    classes = []
    functions = []
    fields = []

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

    def addField(self, field):
        self.fields.append(field)

    def getFields(self):
        return self.fields


class Class:
    name = ""
    description = ""
    functions = []
    fields = []

    def __init__(self, name=None):
        self.name = name

    def getName(self):
        return self.name

    def addFunction(self, func):
        self.functions.append(func)

    def getFunctions(self):
        return self.functions

    def addField(self, field):
        self.fields.append(field)

    def getFields(self):
        return self.fields

    def setDescription(self, desc: str):
        self.description = desc

    def getDescription(self):
        return self.description


class Function:
    description = None
    parameters = []

    def __init__(self, name=""):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, descr: str):
        self.description = descr

    def getDescription(self):
        return self.description

    def addParameter(self, param):
        self.parameters.append(param)

    def getParameters(self):
        return self.parameters


class Field:
    type = "ANY"
    def __init__(self, name=""):
        self.name = name

    def getName(self):
        return self.name

    def setType(self, type: str):
        self.type = type

    def getType(self):
        return self.type


class Parameter:
    description = None
    type = "ANY"

    def __init__(self, name=""):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, descr: str):
        self.description = descr

    def getDescription(self):
        return self.description

    def setType(self, type: str):
        self.type = type

    def getType(self):
        return self.type
