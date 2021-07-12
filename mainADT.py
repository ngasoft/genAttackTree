import parseTree
import parseModel
import genADT
import xml.etree.ElementTree as ET
import os

# two default examples
SD   = "sd"

lib_root = {
    SD   : "Compromise_on-board_computer.xml"
}

def exportToXml(t, example):
    root = ET.Element("adtree")
    root.append(t.toXml())
    ET.ElementTree(root).write(open("output-" + example + ".xml", "wb"))

def main(example, targets):
    print("Loading input model ...")
    Model = parseModel.parseModel("model-" + example + ".inp")

    LibraryFolder = "treelib-" + example
    XMLLibrary = [os.path.join(LibraryFolder, f) for f in os.listdir(LibraryFolder) if f.endswith(".xml") and os.path.isfile(os.path.join(LibraryFolder, f))]
    Library = []

    print("Loading template library ...")

    for xml in XMLLibrary:
        print("Parsing file : " + xml + " ... ")
        r = parseTree.parseXmlTree(xml, Model)
        Library.append(r)


    print("Generating attack trees ...")
    for target in targets:
        t = genADT.genADT(Model, target,Library)

        exportToXml(t, example + "-" + target)

        print("ADS tree for", target, "is exported")
        print("Tree size: " + str(t.size()))
        print("Tree height: " + str(t.height()))

targets = ["OBCOMPUTER","LIDAR", "CAMERA", "GPS", "RADAR", "ECM"] 
main(SD, targets)
import cProfile

