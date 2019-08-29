import parseTree
import parseModel
import genAT
import xml.etree.ElementTree as ET
import os


def exportToXml(t):
    root = ET.Element("sandtree")
    root.append(t.toXml())
    ET.ElementTree(root).write(open("output.xml", "wb"))



LibraryFolder = "treelib"
# XMLLibrary = ["Attack.xml", "Eavesdrop.xml", "EavesdropFrom.xml", "Compromise.xml", "CompromiseFromTo.xml"]
XMLLibrary = [os.path.join(LibraryFolder, f) for f in os.listdir(LibraryFolder) if f.endswith(".xml") and os.path.isfile(os.path.join(LibraryFolder, f))]
XMLRoot = os.path.join(LibraryFolder, "Attack.xml")
RootTree = 0
Library = []

print("Loading template library ...")

for xml in XMLLibrary:
    r = parseTree.parseXmlTree(xml)
    if xml == XMLRoot:
        RootTree = r
    Library.append(r)

print("Loading input model ...")
Model = parseModel.parseModel("model.inp")

t = genAT.genAT(Library, RootTree, Model)

exportToXml(t)

print("Export output")

