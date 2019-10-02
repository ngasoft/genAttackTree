from antlr4 import *
from NodeTemplateParser import NodeTemplateParser
from NodeTemplateListener import NodeTemplateListener
import data

class NodeListener(NodeTemplateListener):

    def __init__(self, node, model):
        self.model = model
        self.node = node

    def enterTree_node(self, ctx:NodeTemplateParser.Tree_nodeContext):
        pass

    def exitTree_node(self, ctx:NodeTemplateParser.Tree_nodeContext):
        self.node.name = ctx.NAME().getText()

    def exitParam(self, ctx:NodeTemplateParser.ParamContext):
        self.node.params.append(self.param)

    def enterVariable(self, ctx:NodeTemplateParser.VariableContext):
        self.variable = data.Variable()

    def exitVariable(self, ctx:NodeTemplateParser.VariableContext):
        self.variable.name = ctx.NAME().getText()
        self.param = self.variable

    def exitVartype(self, ctx:NodeTemplateParser.VartypeContext):
        if ctx.NET():
            self.variable.type = data.CAN
        elif ctx.ECU():
            self.variable.type = data.ECU
        elif ctx.AP():
            self.variable.type = data.ECU
            self.variable.isAP = True

    def exitNetVariable(self, ctx:NodeTemplateParser.NetVariableContext):
        self.variable.on = data.Variable()
        self.variable.on.name = ctx.NAME()
        self.variable.on.type = data.CAN

    def exitNetConstant(self, ctx:NodeTemplateParser.NetConstantContext):
        n = ctx.NAME().getText()
        self.variable.on = self.model[0][n] if n in self.model[0] else None

    def exitConstant(self, ctx:NodeTemplateParser.ConstantContext):
        n = ctx.NAME().getText()
        c = None
        if n in self.model[0]:
            c = self.model[0][n]
        elif n in self.model[1]:
            c = self.model[1][n]
        self.param = c

    def enterGlist(self, ctx:NodeTemplateParser.GlistContext):
        self.listCount = 0
        self.listElement = [None,None]

    def enterEcuVariable(self, ctx:NodeTemplateParser.EcuVariableContext):
        self.variable = data.Variable()

    def exitEcuVariable(self, ctx:NodeTemplateParser.EcuVariableContext):
        self.variable.name = ctx.NAME().getText()
        self.variable.type = data.ECU
        self.variable.isAP = True if ctx.AP() else None
        self.listElement[self.listCount] = self.variable
        self.listCount += 1

    def exitListVariable(self, ctx:NodeTemplateParser.ListVariableContext):
        self.listElement[self.listCount] = data.Variable()
        self.listElement[self.listCount].name = ctx.NAME().getText()
        self.listCount += 1

    def exitEcuConstant(self, ctx:NodeTemplateParser.EcuConstantContext):
        n = ctx.NAME().getText()
        self.listElement[self.listCount] = self.model[1][n] if n in self.model[1] else None
        self.listCount += 1

    def exitUnassigned_list(self, ctx:NodeTemplateParser.Unassigned_listContext):
        self.glist = data.UnassignedList()
        self.glist.begin = self.listElement[0]
        self.glist.end = self.listElement[1]

    def exitAssigned_list(self, ctx:NodeTemplateParser.Assigned_listContext):
        self.glist = data.AssignedList()
        self.glist.head = self.listElement[0]
        self.glist.tail = self.listElement[1]


    def exitGlist(self, ctx:NodeTemplateParser.GlistContext):
        self.param = self.glist

