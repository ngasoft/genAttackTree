import data

def parseModel(modelFile):
    f = open(modelFile, "r")

    cans = {}
    ecus = {}

    line = f.readline().split("#")[0]

    for e in line.split():
        s = e.split(":")
        node = data.GraphNode()
        node.name = s[0]
        node.type = data.ECU
        if len(s) > 1 and s[1] == "AP":
            node.isAP = True
        ecus[node.name] = node

    line = f.readline().split("#")[0]

    for c in line.split():
        node = data.GraphNode()
        node.name = c
        node.type = data.CAN
        cans[node.name] = node

    for c in cans:
        line = f.readline().split("#")[0]
        s = line.split()
        for c in s[1:]:
            cans[s[0]].children.append(ecus[c])

    for c in cans:
        print(cans[c].toString())

    return (cans,ecus)