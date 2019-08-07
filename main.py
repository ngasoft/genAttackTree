import parseTree
import parseModel
import genAT

XMLLibrary = ["Attack.xml", "Eavesdrop.xml", "EavesdropFrom.xml", "Compromise.xml", "CompromiseFromTo.xml", "CompromiseFromTo1.xml"]

Library = []

print("Loading template library ...")

for xml in XMLLibrary:
    r = parseTree.parseXmlTree(xml)
    Library.append(r)

print("Loading input model ...")
Model = parseModel.parseModel("model.inp")

t = genAT.genAT(Library, Model)

print(t.toString())