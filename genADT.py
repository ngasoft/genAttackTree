import data
import xml.etree.ElementTree as ET

n = 1

def exportToXml(t, example):
    global n
    root = ET.Element("sandtree")
    root.append(t.toXml())
    ET.ElementTree(root).write(open("output-" + example + "-" + str(n) + ".xml", "wb"))
    n += 1

def genADT(model, target, library):


    # Stage 1: retrieve or build the initial tree
    tree = buildFrameTree(model, target)
    #exportToXml(tree, "temp")

    # Stage 2: expand the initial tree using templates in the library
    nodes = tree.getNodes()
    while nodes:
        node = nodes.pop()
        subtrees = findMatchingTemplate(node, library) # find a subtree library that match the selected node
        attackSubTrees = filterAttackTrees(subtrees) # attack sub tree is a tree that has at least one attack child
        if attackSubTrees:
            if node.children and node.type != data.OR:
                cnode = node.copy()
                cnode.name += " 1"
                node.type = data.OR
                node.children = [cnode]
                for subtree in attackSubTrees:
                    ctree = subtree.copy() # get a copy of the subtree
                    ctree.name += " #" + str(len(node.children) + 1)
                    node.children.append(ctree)
                    nodes.extend(ctree.getNodes())

            if not node.children or node.type == data.OR:
                for subtree in attackSubTrees:
                    ctree = subtree.copy() # get a copy of the subtree
                    ctree.name += " #" + str(len(node.children) + 1)
                    node.children.append(ctree)
                    nodes.extend(ctree.getNodes())
        for subtree in subtrees:
            if subtree not in attackSubTrees:
                for subChild in subtree.children:
                    ctree = subChild.copy()
                    node.children.append(ctree)
                    nodes.extend(ctree.getNodes())

        #exportToXml(tree, "temp")


    return tree

def findMatchingTemplate(leaf, library):
    matchedTrees = []
    for tree in library:
        if leaf.name == tree.name:
            matchedTrees.append(tree)
    return matchedTrees

def filterAttackTrees(trees):
    attackTrees = []
    for tree in trees:
        isAT = False
        for child in tree.children:
            if child.po_type == data.PRO:
                isAT = True
            else:
                isAT = False
                break
        if isAT:
            attackTrees.append(tree)

    return attackTrees

def buildFrameTree(model, target):
    (networks, components) = model
    visited_networks = []
    visited_components = []
    target_component = components[target]

    root = data.TreeNode()
    root.name = "Compromise " + target

    queue = [(root,networks[network]) for network in networks if target_component in networks[network].children]
    visited_components.append(target_component)

    while queue:
        (tree, e) = queue.pop()
        subtree = data.TreeNode()
        subtree.name = "Compromise " + e.name
        tree.children.append(subtree)
        if e.name in networks:
            visited_networks.append(e)
            for c in e.children:
                if c not in visited_components:
                    queue.append((subtree,c))
        else:
            visited_components.append(e)
            for n in networks:
                if networks[n] not in visited_networks and e in networks[n].children:
                    queue.append((subtree,networks[n]))

    return root                  





