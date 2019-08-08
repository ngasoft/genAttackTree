# data structure for tree node
import xml.etree.ElementTree as ET


ANY = -1
OR = 0
AND = 1
SAND = 2
CAN = 3
ECU = 4

def getXmlRefinement(n):
    if n==OR:
        return "disjunctive"
    if n==AND:
        return "conjunctive"
    if n==SAND:
        return "sequential"
    return "UR"

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
        for i in range(len(self.params)):
            p = self.params[i]
            if isinstance(p, Variable):
                for j in range(len(assignment[0])):
                    if assignment[0][j].name == p.name:
                        self.params[i] = assignment[1][j]
            p = self.params[i]
            if isinstance(p, Variable) and  isinstance(p.on, Variable):
                for j in range(len(assignment[0])):
                    if assignment[0][j].name == p.on.name:
                        p.on = assignment[1][j]
            if isinstance(p, Variable):
                for k in range(len(p.diff)):
                    d = p.diff[k]
                    if isinstance(d, Variable):
                        for j in range(len(assignment[0])):
                            if assignment[0][j].name == d.name:
                                p.diff[k] = assignment[1][j]
        for c in self.children:
            c.applyAssignment(assignment)

    def match(self, node):
        if node.name != self.name:
            return None
        sub = ([],[])
        for i in range(len(self.params)):
            if isinstance(node.params[i], Variable) and isinstance(self.params[i], GraphNode):
                sub[0].append(node.params[i])
                sub[1].append(self.params[i])
            elif isinstance(node.params[i], GraphNode) and isinstance(self.params[i], GraphNode):
                if node.params[i].name != self.params[i].name:
                    return None
        return sub

    def toXml(self):
        root = ET.Element("node")
        root.set("refinement", getXmlRefinement(self.type))
        label = ET.Element("label")
        label.text = self.name + "(" + ",".join([p.name for p in self.params]) + ")"
        root.append(label)
        for c in self.children:
            root.append(c.toXml())
        return root


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

