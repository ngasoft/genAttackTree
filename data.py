# data structure for tree node
import xml.etree.ElementTree as ET


ANY = -1
OR = 0
AND = 1
SAND = 2
CAN = 3
ECU = 4
PRO = 5
OPP = 6

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
        self.type = OR
        self.po_type = PRO # identify the node is of type proponent or opponent
        self.name = ""
        self.params = []
        self.children = []

    def copy(self):
        c = TreeNode()
        c.type = self.type
        c.po_type = self.po_type
        c.name = self.name
        c.params = [p.copy() for p in self.params]
        c.children = [ch.copy() for ch in self.children]
        return c

    def size(self):
        return 1 + sum([c.size() for c in self.children])

    def height(self):
        return 1 + (max([c.height() for c in self.children]) if self.children else 0)

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

    def getNodes(self):
        nodes = [self]
        if self.children:
            for c in self.children:
                nodes += c.getNodes()
        return nodes


    def toXml(self):
        root = ET.Element("node")
        root.set("refinement", getXmlRefinement(self.type))
        if self.po_type==OPP:
            root.set("switchRole", "yes")
        label = ET.Element("label")
        params = "(" + ",".join([listToString(p) if isinstance(p, list) else p.toString()  for p in self.params]) + ")" if self.params else ""
        label.text = self.name + params
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
        # if self.isAP:
        #     s += (":AP")
        # s += ":" + rdata(self.type)
        # s += "("
        # for c in self.children:
        #     s += c.toString()
        #     s += ", "
        # if s[-2:] == ", ":
        #     s = s[:-2]
        # s += ")"
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


def listToString(l):
    return "["+ ",".join([i.toString() for i in l]) +"]"

Library = None
Tree = None

