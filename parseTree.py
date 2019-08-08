import data
import xml.etree.ElementTree as ET


ORNODE = "disjunctive"
ANDNODE = "conjunctive"
SANDNODE = "sequential"

def parseXmlTree(xmlFile):
    tree = ET.parse(xmlFile)
    doc = list(tree.getroot())[0]

    rootNode = parseXmlNode(doc)
    print(rootNode.toString())

    return rootNode

def parseXmlNode(n):
    t = data.TreeNode()
    if n.get("refinement")==ORNODE:
        t.type = data.OR
    if n.get("refinement")==ANDNODE:
        t.type = data.AND
    if n.get("refinement")==SANDNODE:
        t.type = data.SAND
    children = list(n)
    labels = children[0].text.split()
    t.name = labels[0]
    parseParams(t, labels[1:])

    for c in children[1:]:
        t.children.append(parseXmlNode(c))
    return t


def parseParams(t, tokens):
    if len(tokens) == 0:
        return
    if tokens[0] == "[":
        if tokens[2] == "|":
            p = data.AssignedList()
            p.head = parseVar(tokens[1])
            p.tail = parseVar(tokens[3])
            t.params.append(p)
        elif tokens[2] == "..":
            p = data.UnassignedList()
            p.begin = parseVar(tokens[1])
            p.end = parseVar(tokens[3])
            t.params.append(p)
        else:
            p = data.SingletonList()
            p.element = parseVar(tokens[1])
            t.params.append(p)
        parseParams(t, tokens[5:])
    else:
        v = parseVar(tokens[0])
        t.params.append(v)
        parseParams(t, tokens[1:])

def parseVar(token):
    on = token.split("/")
    v = parseVar1(on[0])
    if len(on)>1:
        v1 = parseVar1(on[1])
        v.on = v1
    return v

def parseVar1(token):
    v = data.Variable()
    t = token.split(":")
    v.name = t[0]
    if len(t)>=2:
        if t[1]!="AP":
            v.type = data.CAN if t[1]=="CAN" else data.ECU
            if len(t)>=3 and t[2]=="AP":
                v.isAP = True
        else:
            v.type = data.ECU
            v.isAP = True
    return v

# r = parseXmlTree("Attack.xml")
# r = parseXmlTree("Eavesdrop.xml")
# r = parseXmlTree("EavesdropFrom.xml")
# r = parseXmlTree("Compromise.xml")
# r = parseXmlTree("CompromiseFromTo.xml")
# r = parseXmlTree("CompromiseFromTo1.xml")
