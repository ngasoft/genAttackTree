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

    def copy(self):
        c = TreeNode()
        c.type = self.type
        c.name = self.name
        c.params = [p.copy() for p in self.params]
        c.children = [ch.copy() for ch in self.children]
        return c

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
            if isinstance(p, UnassignedList):
                for i in range(len(assignment[0])):
                    var = assignment[0][i]
                    val = assignment[1][i]
                    if isinstance(var, UnassignedList) and var.begin.name==p.begin.name and var.end.name==p.end.name:
                        self.params[i] = val
                if isinstance(p.begin, Variable):
                    for j in range(len(assignment[0])):
                        if isinstance(assignment[0][j],Variable) and assignment[0][j].name == p.begin.name:
                            p.begin = assignment[1][j]
                if isinstance(p.end, Variable):
                    for j in range(len(assignment[0])):
                        if isinstance(assignment[0][j],Variable) and assignment[0][j].name == p.end.name:
                            p.end = assignment[1][j]
            if isinstance(p, AssignedList):
                if isinstance(p.head, Variable):
                    for j in range(len(assignment[0])):
                        if isinstance(assignment[0][j], Variable) and assignment[0][
                            j].name == p.head.name:
                            p.head = assignment[1][j]
                if isinstance(p.tail, Variable):
                    for j in range(len(assignment[0])):
                        if isinstance(assignment[0][j], Variable) and assignment[0][
                            j].name == p.tail.name:
                            p.tail = assignment[1][j]

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
            if isinstance(node.params[i], AssignedList) and len(self.params[i]) <= 0:
                return None
            if isinstance(node.params[i], AssignedList) and isinstance(self.params[i], list) and len(self.params[i])>0:
                sub[0].append(node.params[i].head)
                sub[1].append(self.params[i][0])
                sub[0].append(node.params[i].tail)
                sub[1].append(self.params[i][1:])
            elif isinstance(node.params[i], GraphNode) and isinstance(self.params[i], GraphNode):
                if node.params[i].name != self.params[i].name:
                    return None
        return sub

    def toXml(self):
        root = ET.Element("node")
        root.set("refinement", getXmlRefinement(self.type))
        label = ET.Element("label")
        label.text = self.name + "(" + ",".join([listToString(p) if isinstance(p, list) else p.toString()  for p in self.params]) + ")"
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

    def copy(self):
        return self

class Variable:
    def __init__(self):
        self.name = ""
        self.type = ANY
        self.on = None
        self.diff = []
        self.isAP = False

    def copy(self):
        v = Variable()
        v.name = self.name
        v.type = self.type
        v.on = self.on.copy() if self.on else None
        v.diff = [d.copy() for d in self.diff]
        v.isAP = self.isAP
        return v


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
        self.name  = "UnassignedList_ShouldNotMatchWithVariableName"

    def toString(self):
        s = "[" + self.begin.toString() + ".." + self.end.toString() + "]"
        return s

    def copy(self):
        l = UnassignedList()
        l.begin = self.begin.copy() if self.begin else None
        l.end = self.end.copy() if self.end else None
        return l

class AssignedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.name = "AssignedList_ShouldNotMatchWithVariableName"

    def toString(self):
        tailText = self.tail.toString() if isinstance(self.tail, Variable) else listToString(self.tail)
        s = "[" + self.head.toString() + "|" + str(tailText) + "]"
        return s


    def copy(self):
        l = AssignedList()
        l.head = self.head.copy() if self.head else None
        l.tail = self.tail.copy() if self.tail else None
        return l



def listToString(l):
    return "["+ ",".join([i.toString() for i in l]) +"]"

Library = None
Tree = None

