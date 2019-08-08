import copy
import data
import xml.etree.ElementTree as ET


def genAT(library, model):
    tree = copy.deepcopy(library[0])

    while True:

        # get all leaves of the tree
        leaves = tree.getLeaves()

        # find a leaf in leaves and a tree in Library
        # such that they can match
        found = False
        for leaf in leaves:
            leaf.type = data.OR # turn leaf into an or node

            assignments = findAssignments(leaf, model) # find all assigments for leaf
            if assignments == []:
                assignments = [[]]
            for assignment in assignments:
                cleaf = copy.deepcopy(leaf)
                cleaf.applyAssignment(assignment)
                (subtree, sub) = findTree(cleaf, library) # find a subtree library that match leaf(assignment) by a substitution
                if subtree != None:
                    found = True
                    ctree = copy.deepcopy(subtree) # get a copy of the subtree
                    ctree.applyAssignment(sub)
                    leaf.children.append(ctree)

        if not found:
            break

    return tree

def findTree(leaf, library):
    for tree in library:
        sub = leaf.match(tree)
        if sub != None:
            return (tree, sub)
    return (None, None)



# find all assignment of a leaf wrt a model
def findAssignments(leaf, model):
    variables = []
    values = []
    for p in leaf.params:
        v = []
        if isinstance(p, data.Variable):
            variables.append(p)
            v = findValues(p, model)
        if isinstance(p, data.UnassignedList):
            variables.append(p)
            v = findPaths(p.begin, p.end, model)
        if not v:
            return []
        values.append(v)
    assignments = []
    a = [0 for v in values]
    while a:
        assignment = (variables, [values[i][a[i]] for i in range(len(values))])
        assignments.append(assignment)
        a = getNextAssignment(a, values)

    return assignments

def findPaths(begin, end, model):
    v0 = []
    if isinstance(begin, data.Variable):
        v0 = findValues(begin, model)
    elif isinstance(begin, data.GraphNode):
        v0 = [begin]
    v1 = []
    if isinstance(end, data.Variable):
        v1 = findValues(end, model)
    elif isinstance(end, data.GraphNode):
        v1 = [end]

    paths = []
    for s in v0:
        paths += dfs([s], v1, model) # depth first search

    return paths

def dfs(path, finals, model):
    nexts = getNexts(path, model)
    r = []
    for n in nexts:
        found = False
        for m in finals:
            if n.name == m.name:
                found = True
                path1 = path + [n]
                r.append(path1)
        if not found:
            path1 = path + [n]
            r += dfs(path1, finals, model)
    return r

def getNexts(path, model):
    last = path[-1]
    cans = [c for c in model[0].keys() if last in model[0][c].children]
    nexts = []
    for c in cans:
        nexts += model[0][c].children
    return [n for n in nexts if n not in path]

def findValues(p, model):
    if p.type == data.ECU:
        if p.on:
            v = getCAN(p.on, model)
        else:
            v = [model[1][k] for k in model[1].keys()]
    elif p.type == data.CAN:
        v = [model[0][k] for k in model[0].keys()]
    else:
        v = [model[0][k] for k in model[0].keys()] + [model[1][k] for k in model[1].keys()]
    if p.diff:
        v = removeDiff(v, p.diff)
    if p.isAP:
        v = [n for n in v if n.isAP]
    return v


def getNextAssignment(a, values):
    for i in range(len(a)):
        if a[i] < len(values[i]) - 1:
            a[i] = a[i] + 1
            for j in range(i):
                a[j] = 0
            return a
    return None

def getCAN(node, model):
    if node.type == data.CAN:
        return copy.copy(model[0][node.name].children)
    else:
        for c in model[0]:
            if node in model[0][c].children:
                return copy.copy(model[0][c].children)

def removeDiff(v, diff):
    for d in diff:
        v.remove(d)
    return v



