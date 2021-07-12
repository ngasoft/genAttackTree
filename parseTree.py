from antlr4 import *
from NodeTemplateLexer import NodeTemplateLexer
from NodeTemplateParser import NodeTemplateParser
from parseListener import NodeListener as NodeListener

import data
import xml.etree.ElementTree as ET


ORNODE = "disjunctive"
ANDNODE = "conjunctive"
SANDNODE = "sequential"

def parseXmlTree(xmlFile, model):
    tree = ET.parse(xmlFile)
    doc = list(tree.getroot())[0]

    rootNode = parseXmlNode(doc, model)
    print(rootNode.toString())

    return rootNode

def parseXmlNode(n, model):
    children = list(n)
    # print("Parsing text : " + children[0].text)
    t = parseADTNode(children[0].text, model)
    if n.get("refinement")==ORNODE:
        t.type = data.OR
    if n.get("refinement")==ANDNODE:
        t.type = data.AND
    if n.get("refinement")==SANDNODE:
        t.type = data.SAND

    if n.get("switchRole")=="yes":
        t.po_type = data.OPP
    else:
        t.po_type = data.PRO

    for c in children[1:]:
        t.children.append(parseXmlNode(c, model))
    return t

def parseNode(text, model):
    lexer = NodeTemplateLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = NodeTemplateParser(stream)
    tree = parser.tree_node()

    node = data.TreeNode()
    nodeListener = NodeListener(node, model)
    walker = ParseTreeWalker()
    walker.walk(nodeListener, tree)
    return node

def parseADTNode(text, model):
    node = data.TreeNode()
    node.name = text
    return node


# r = parseXmlTree("Attack.xml")
# r = parseXmlTree("Eavesdrop.xml")
# r = parseXmlTree("EavesdropFrom.xml")
# r = parseXmlTree("Compromise.xml")
# r = parseXmlTree("CompromiseFromTo.xml")
# r = parseXmlTree("CompromiseFromTo1.xml")
