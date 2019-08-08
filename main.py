import parseTree
import parseModel
import genAT
import xml.etree.ElementTree as ET


def exportToXml(t):
    root = ET.Element("sandtree")
    root.append(t.toXml())
    ET.ElementTree(root).write(open("output.xml", "wb"))


XMLLibrary = ["Attack.xml", "Eavesdrop.xml", "EavesdropFrom.xml", "Compromise.xml", "CompromiseFromTo.xml"]

Library = []

print("Loading template library ...")

for xml in XMLLibrary:
    r = parseTree.parseXmlTree(xml)
    Library.append(r)

print("Loading input model ...")
Model = parseModel.parseModel("model.inp")

t = genAT.genAT(Library, Model)

exportToXml(t)

print("Export output")

