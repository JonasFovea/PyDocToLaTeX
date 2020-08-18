class Doc:
    name = ""
    description = ""
    classes = []
    functions = []
    fields = []

    def __init__(self, name: str):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, desc: str):
        self.description = desc

    def getDescription(self):
        return self.description

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

    def buildFrame(self):
        if len(self.description) == 0:
            return "\section{" + self.name + "}\n"
        return "\section{" + self.name + "}\n" + self.description + "\n"

    def buildFields(self):
        s = "\subsection{Fields}\n\\begin{tabular}{|l|l|l|}\hline\n"
        s += "\t\\textbf{name} & \\textbf{type} & \\textbf{description}\\\\\\hline\n"
        for f in self.fields:
            s += "\t" + f.getName().replace("_","\\_") + " & " + f.getType() + " & " + f.getDescription() + " \\\\\\hline\n"
        s += "\end{tabular}\n"
        return s

    def buildClasses(self):
        s = "\\subsection{Classes}\n"
        for c in self.classes:
            s += "\\subsubsection{" + c.getName() + "}\n"
            s += "\\textbf{Fields}\\\\[0.5\\baselineskip]\n"
            s += "\\begin{tabular}{|p{0.4\\linewidth}|p{0.1\\linewidth}|p{0.5\\linewidth}|}\\hline\n"
            s += "\\textbf{name} & \\textbf{type} & \\textbf{description}\\\\\\hline\n"
            for field in c.getFields():
                s += field.getName() + " & " + field.getType() + " & " + field.getDescription() + "\\\\\\hline\n"
            s += "\\end{tabular}\\\\[\\baselineskip]\n"

            s += "\\textbf{Functions}\\\\[0.5\\baselineskip]\n"
            s += "\\begin{tabular}{|p{0.15\\linewidth}|p{0.35\\linewidth}|p{0.5\\linewidth}|}\\hline\n"
            s += "\\textbf{name} & \\textbf{parameters} & \\textbf{description}\\\\\\hline\n"
            for func in c.getFunctions():
                s += func.getName().replace("_","\\_") + " & \\begin{minipage}{\\textwidth}\\begin{itemize}"
                for param in func.getParameters():
                    s += "\\item " + param.getType() + " " + param.getName() + " :: " + param.getDescription() + " "
                s += "\\end{itemize}\\end{minipage}"
                s += " & " + func.getDescription() + "\\\\\\hline\n"
            s += "\\end{tabular}\\\\\n"

        return s

    def exportFile(self, fileName):
        content = self.buildFrame()
        if len(self.fields) > 0:
            content += self.buildFields()
        if len(self.classes) > 0:
            content += self.buildClasses()
        f = open(fileName, "w")
        f.write(content)
        f.close()


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
    name = ""

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
    description = ""

    def __init__(self, name=""):
        self.name = name

    def getName(self):
        return self.name

    def setType(self, type: str):
        self.type = type

    def getType(self):
        return self.type

    def setDescription(self, desc: str):
        self.description = desc

    def getDescription(self):
        return self.description


class Parameter:
    description = ""
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
