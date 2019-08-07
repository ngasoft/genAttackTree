import copy

def genAT(library, model):
    tree = copy.deepcopy(library[0])

    while True:

        # get all leaves of the tree
        leaves = tree.getLeaves()

        # find a leaf in leaves and a tree in Library
        # such that they can match
        found = False
        for leaf in leaves:
            for subtree in library:
                if leaf matches subtree:
                    found = True
                    find all assignments for variables in subtree
                    turn leaf in to an or node
                    for assignment in assignments:
                        get a copy of the subtree
                        apply the assignment to the copied subtree
                        add the applied subtree as a child of leaf

        if not found:
            break

    return tree