import copy
import data

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
                assignments == [[]]
            for assignment in assignments:
                cleaf = copy.deepcopy(leaf)
                cleaf.applyAssignment(assignment)
                (tree, sub) = findTree(cleaf, library) # find a subtree library that match leaf(assignment) by a substitution
                found = True
                ctree = copy.deepcopy(tree) # get a copy of the subtree
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
    return None



# find all assignment of a leaf wrt a model
def findAssignments(leaf, model):
    variables = []
    values = []
    for p in leaf.params:
        if isinstance(p, data.Variable):
            variables.append(p)
            v = []
            if p.type==data.ECU:
                if p.on:
                    v = getCAN(p.on, model)
                else:
                    v = copy.copy(model[1])
            elif p.type==data.CAN:
                v = copy.copy(model[0])
            else:
                v = copy.copy(model[0]) + copy.copy(model[1])
            if p.diff:
                v = removeDiff(v, p.diff)
            values.append(v)
            if not v:
                return []
    assignments = []
    a = [0 for v in values]
    while a:
        assignment = (variables, [values[i][list(values[i].keys())[a[i]]] for i in range(len(values))])
        assignments.append(assignment)
        a = getNextAssignment(a, values)

    return assignments

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



