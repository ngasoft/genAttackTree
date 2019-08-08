# data structure for tree node


ANY = -1
OR = 0
AND = 1
SAND = 2
CAN = 3
ECU = 4

def rdata(n):
    if n==OR:
        return "OR"
    if n==AND:
        return "AND"
    if n==SAND:
        return "SAND"
    if n==CAN:
        return "CAN"
    if n==ECU:
        return "ECU"
    if n==ANY:
        return "ANY"
    return "UR"

class TreeNode:

    def __init__(self):
        self.type = ANY
        self.name = ""
        self.params = []
        self.children = []

    def toString(self):
        s = self.name + "#"
        for p in self.params:
            s += p.toString() + "#"
        s += rdata(self.type)
        s += "("
        for c in self.children:
            s += c.toString()
            s += ", "
        if s[-2:] == ", ":
            s = s[:-2]
        s += ")"
        return s

    def getLeaves(self):
        if self.children:
            leaves = []
            for c in self.children:
                leaves += c.getLeaves()
            return leaves
        else:
            return [self]

    def applyAssignment(self, assignment):
        for i in len(self.params):
            p = p[i]
            if isinstance(p, Variable):
                for j in len(assignment):
                    if assignment[0][j].name == p.name:
                        p[i] = assignment[1][j]

    def match(self, node):
        if node.name != self.name:
            return None
        sub = [[],[]]
        for i in len(self.params):
            if isinstance(node.params[i], Variable) and isinstance(self.params[i], GraphNode):
                sub[0].append(node.params[i])
                sub[1].append(self.params[i])
            elif isinstance(node.params[i], GraphNode) and isinstance(self.params[i], GraphNode):
                if node.params[i].name != self.params[i].name:
                    return None
        return sub



class GraphNode:

    def __init__(self):
        self.name = ""
        self.type = ANY
        self.children = []
        self.isAP = False # True, False

    def toString(self):
        s = self.name
        if self.isAP:
            s += (":AP")
        s += ":" + rdata(self.type)
        s += "("
        for c in self.children:
            s += c.toString()
            s += ", "
        if s[-2:] == ", ":
            s = s[:-2]
        s += ")"
        return s

class Variable:
    def __init__(self):
        self.name = ""
        self.type = ANY
        self.on = None
        self.diff = []

    def toString(self):
        s = self.name
        s += ":" + rdata(self.type)
        if self.on:
            s += "/" + self.on.toString()
        return s

class UnassignedList:

    def __init__(self):
        self.begin = None
        self.end   = None

    def toString(self):
        s = "[" + self.begin.toString() + ".." + self.end.toString() + "]"
        return s

class AssignedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def toString(self):
        s = "[" + self.head.toString() + "|" + self.tail.toString() + "]"
        return s

class SingletonList:

    def __init__(self):
        self.element = None

    def toString(self):
        s = "[" + self.element.toString() + "]"
        return s

Library = None
Tree = None

