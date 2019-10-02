# Generated from C:/Users/ac1222/OneDrive - Coventry University/GitHub/genAT\NodeTemplate.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\3\2\3\2\7\2#\n\2\f\2\16\2&\13\2")
        buf.write("\5\2(\n\2\3\3\3\3\3\3\5\3-\n\3\3\4\3\4\3\4\5\4\62\n\4")
        buf.write("\3\4\3\4\5\4\66\n\4\3\5\3\5\3\6\3\6\5\6<\n\6\3\7\3\7\5")
        buf.write("\7@\n\7\3\b\3\b\3\b\5\bE\n\b\3\b\3\b\3\b\5\bJ\n\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\nW\n\n\3\13")
        buf.write("\3\13\3\13\5\13\\\n\13\3\13\3\13\5\13`\n\13\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\2\2\20\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\2\4\3\2\r\17\3\2\16")
        buf.write("\17\2k\2\36\3\2\2\2\4,\3\2\2\2\6.\3\2\2\2\b\67\3\2\2\2")
        buf.write("\n;\3\2\2\2\f?\3\2\2\2\16A\3\2\2\2\20M\3\2\2\2\22S\3\2")
        buf.write("\2\2\24X\3\2\2\2\26a\3\2\2\2\30c\3\2\2\2\32f\3\2\2\2\34")
        buf.write("i\3\2\2\2\36\'\7\20\2\2\37$\5\4\3\2 !\7\3\2\2!#\5\4\3")
        buf.write("\2\" \3\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%(\3\2\2\2")
        buf.write("&$\3\2\2\2\'\37\3\2\2\2\'(\3\2\2\2(\3\3\2\2\2)-\5\6\4")
        buf.write("\2*-\5\f\7\2+-\5\30\r\2,)\3\2\2\2,*\3\2\2\2,+\3\2\2\2")
        buf.write("-\5\3\2\2\2.\61\7\20\2\2/\60\7\4\2\2\60\62\5\b\5\2\61")
        buf.write("/\3\2\2\2\61\62\3\2\2\2\62\65\3\2\2\2\63\64\7\5\2\2\64")
        buf.write("\66\5\n\6\2\65\63\3\2\2\2\65\66\3\2\2\2\66\7\3\2\2\2\67")
        buf.write("8\t\2\2\28\t\3\2\2\29<\5\32\16\2:<\5\22\n\2;9\3\2\2\2")
        buf.write(";:\3\2\2\2<\13\3\2\2\2=@\5\20\t\2>@\5\16\b\2?=\3\2\2\2")
        buf.write("?>\3\2\2\2@\r\3\2\2\2AD\7\6\2\2BE\5\24\13\2CE\5\34\17")
        buf.write("\2DB\3\2\2\2DC\3\2\2\2EF\3\2\2\2FI\7\21\2\2GJ\5\24\13")
        buf.write("\2HJ\5\34\17\2IG\3\2\2\2IH\3\2\2\2JK\3\2\2\2KL\7\7\2\2")
        buf.write("L\17\3\2\2\2MN\7\6\2\2NO\5\24\13\2OP\7\b\2\2PQ\5\26\f")
        buf.write("\2QR\7\7\2\2R\21\3\2\2\2SV\7\20\2\2TU\7\4\2\2UW\7\r\2")
        buf.write("\2VT\3\2\2\2VW\3\2\2\2W\23\3\2\2\2X[\7\20\2\2YZ\7\4\2")
        buf.write("\2Z\\\t\3\2\2[Y\3\2\2\2[\\\3\2\2\2\\_\3\2\2\2]^\7\5\2")
        buf.write("\2^`\5\n\6\2_]\3\2\2\2_`\3\2\2\2`\25\3\2\2\2ab\7\20\2")
        buf.write("\2b\27\3\2\2\2cd\7\t\2\2de\7\20\2\2e\31\3\2\2\2fg\7\t")
        buf.write("\2\2gh\7\20\2\2h\33\3\2\2\2ij\7\t\2\2jk\7\20\2\2k\35\3")
        buf.write("\2\2\2\16$\',\61\65;?DIV[_")
        return buf.getvalue()


class NodeTemplateParser ( Parser ):

    grammarFileName = "NodeTemplate.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'/'", "'['", "']'", "'|'", 
                     "'@'", "'AND'", "'OR'", "'SAND'", "'NET'", "'ECU'", 
                     "'AP'", "<INVALID>", "'..'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "AND", "OR", "SAND", "NET", "ECU", "AP", "NAME", "DCOLON", 
                      "WS" ]

    RULE_tree_node = 0
    RULE_param = 1
    RULE_variable = 2
    RULE_vartype = 3
    RULE_net = 4
    RULE_glist = 5
    RULE_unassigned_list = 6
    RULE_assigned_list = 7
    RULE_netVariable = 8
    RULE_ecuVariable = 9
    RULE_listVariable = 10
    RULE_constant = 11
    RULE_netConstant = 12
    RULE_ecuConstant = 13

    ruleNames =  [ "tree_node", "param", "variable", "vartype", "net", "glist", 
                   "unassigned_list", "assigned_list", "netVariable", "ecuVariable", 
                   "listVariable", "constant", "netConstant", "ecuConstant" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    AND=8
    OR=9
    SAND=10
    NET=11
    ECU=12
    AP=13
    NAME=14
    DCOLON=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Tree_nodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(NodeTemplateParser.NAME, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeTemplateParser.ParamContext)
            else:
                return self.getTypedRuleContext(NodeTemplateParser.ParamContext,i)


        def getRuleIndex(self):
            return NodeTemplateParser.RULE_tree_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTree_node" ):
                listener.enterTree_node(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTree_node" ):
                listener.exitTree_node(self)




    def tree_node(self):

        localctx = NodeTemplateParser.Tree_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tree_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(NodeTemplateParser.NAME)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NodeTemplateParser.T__3) | (1 << NodeTemplateParser.T__6) | (1 << NodeTemplateParser.NAME))) != 0):
                self.state = 29
                self.param()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NodeTemplateParser.T__0:
                    self.state = 30
                    self.match(NodeTemplateParser.T__0)
                    self.state = 31
                    self.param()
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(NodeTemplateParser.VariableContext,0)


        def glist(self):
            return self.getTypedRuleContext(NodeTemplateParser.GlistContext,0)


        def constant(self):
            return self.getTypedRuleContext(NodeTemplateParser.ConstantContext,0)


        def getRuleIndex(self):
            return NodeTemplateParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = NodeTemplateParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_param)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NodeTemplateParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.variable()
                pass
            elif token in [NodeTemplateParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.glist()
                pass
            elif token in [NodeTemplateParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(NodeTemplateParser.NAME, 0)

        def vartype(self):
            return self.getTypedRuleContext(NodeTemplateParser.VartypeContext,0)


        def net(self):
            return self.getTypedRuleContext(NodeTemplateParser.NetContext,0)


        def getRuleIndex(self):
            return NodeTemplateParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = NodeTemplateParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(NodeTemplateParser.NAME)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NodeTemplateParser.T__1:
                self.state = 45
                self.match(NodeTemplateParser.T__1)
                self.state = 46
                self.vartype()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NodeTemplateParser.T__2:
                self.state = 49
                self.match(NodeTemplateParser.T__2)
                self.state = 50
                self.net()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NET(self):
            return self.getToken(NodeTemplateParser.NET, 0)

        def ECU(self):
            return self.getToken(NodeTemplateParser.ECU, 0)

        def AP(self):
            return self.getToken(NodeTemplateParser.AP, 0)

        def getRuleIndex(self):
            return NodeTemplateParser.RULE_vartype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVartype" ):
                listener.enterVartype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVartype" ):
                listener.exitVartype(self)




    def vartype(self):

        localctx = NodeTemplateParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NodeTemplateParser.NET) | (1 << NodeTemplateParser.ECU) | (1 << NodeTemplateParser.AP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def netConstant(self):
            return self.getTypedRuleContext(NodeTemplateParser.NetConstantContext,0)


        def netVariable(self):
            return self.getTypedRuleContext(NodeTemplateParser.NetVariableContext,0)


        def getRuleIndex(self):
            return NodeTemplateParser.RULE_net

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNet" ):
                listener.enterNet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNet" ):
                listener.exitNet(self)




    def net(self):

        localctx = NodeTemplateParser.NetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_net)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NodeTemplateParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.netConstant()
                pass
            elif token in [NodeTemplateParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.netVariable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigned_list(self):
            return self.getTypedRuleContext(NodeTemplateParser.Assigned_listContext,0)


        def unassigned_list(self):
            return self.getTypedRuleContext(NodeTemplateParser.Unassigned_listContext,0)


        def getRuleIndex(self):
            return NodeTemplateParser.RULE_glist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlist" ):
                listener.enterGlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlist" ):
                listener.exitGlist(self)




    def glist(self):

        localctx = NodeTemplateParser.GlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_glist)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.assigned_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.unassigned_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unassigned_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DCOLON(self):
            return self.getToken(NodeTemplateParser.DCOLON, 0)

        def ecuVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeTemplateParser.EcuVariableContext)
            else:
                return self.getTypedRuleContext(NodeTemplateParser.EcuVariableContext,i)


        def ecuConstant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NodeTemplateParser.EcuConstantContext)
            else:
                return self.getTypedRuleContext(NodeTemplateParser.EcuConstantContext,i)


        def getRuleIndex(self):
            return NodeTemplateParser.RULE_unassigned_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnassigned_list" ):
                listener.enterUnassigned_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnassigned_list" ):
                listener.exitUnassigned_list(self)




    def unassigned_list(self):

        localctx = NodeTemplateParser.Unassigned_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unassigned_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(NodeTemplateParser.T__3)
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NodeTemplateParser.NAME]:
                self.state = 64
                self.ecuVariable()
                pass
            elif token in [NodeTemplateParser.T__6]:
                self.state = 65
                self.ecuConstant()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 68
            self.match(NodeTemplateParser.DCOLON)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NodeTemplateParser.NAME]:
                self.state = 69
                self.ecuVariable()
                pass
            elif token in [NodeTemplateParser.T__6]:
                self.state = 70
                self.ecuConstant()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 73
            self.match(NodeTemplateParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assigned_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ecuVariable(self):
            return self.getTypedRuleContext(NodeTemplateParser.EcuVariableContext,0)


        def listVariable(self):
            return self.getTypedRuleContext(NodeTemplateParser.ListVariableContext,0)


        def getRuleIndex(self):
            return NodeTemplateParser.RULE_assigned_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigned_list" ):
                listener.enterAssigned_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigned_list" ):
                listener.exitAssigned_list(self)




    def assigned_list(self):

        localctx = NodeTemplateParser.Assigned_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assigned_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(NodeTemplateParser.T__3)
            self.state = 76
            self.ecuVariable()
            self.state = 77
            self.match(NodeTemplateParser.T__5)
            self.state = 78
            self.listVariable()
            self.state = 79
            self.match(NodeTemplateParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetVariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(NodeTemplateParser.NAME, 0)

        def NET(self):
            return self.getToken(NodeTemplateParser.NET, 0)

        def getRuleIndex(self):
            return NodeTemplateParser.RULE_netVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetVariable" ):
                listener.enterNetVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetVariable" ):
                listener.exitNetVariable(self)




    def netVariable(self):

        localctx = NodeTemplateParser.NetVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_netVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(NodeTemplateParser.NAME)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NodeTemplateParser.T__1:
                self.state = 82
                self.match(NodeTemplateParser.T__1)
                self.state = 83
                self.match(NodeTemplateParser.NET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EcuVariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(NodeTemplateParser.NAME, 0)

        def net(self):
            return self.getTypedRuleContext(NodeTemplateParser.NetContext,0)


        def ECU(self):
            return self.getToken(NodeTemplateParser.ECU, 0)

        def AP(self):
            return self.getToken(NodeTemplateParser.AP, 0)

        def getRuleIndex(self):
            return NodeTemplateParser.RULE_ecuVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEcuVariable" ):
                listener.enterEcuVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEcuVariable" ):
                listener.exitEcuVariable(self)




    def ecuVariable(self):

        localctx = NodeTemplateParser.EcuVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ecuVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(NodeTemplateParser.NAME)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NodeTemplateParser.T__1:
                self.state = 87
                self.match(NodeTemplateParser.T__1)
                self.state = 88
                _la = self._input.LA(1)
                if not(_la==NodeTemplateParser.ECU or _la==NodeTemplateParser.AP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NodeTemplateParser.T__2:
                self.state = 91
                self.match(NodeTemplateParser.T__2)
                self.state = 92
                self.net()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListVariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(NodeTemplateParser.NAME, 0)

        def getRuleIndex(self):
            return NodeTemplateParser.RULE_listVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListVariable" ):
                listener.enterListVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListVariable" ):
                listener.exitListVariable(self)




    def listVariable(self):

        localctx = NodeTemplateParser.ListVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_listVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(NodeTemplateParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(NodeTemplateParser.NAME, 0)

        def getRuleIndex(self):
            return NodeTemplateParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = NodeTemplateParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(NodeTemplateParser.T__6)
            self.state = 98
            self.match(NodeTemplateParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NetConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(NodeTemplateParser.NAME, 0)

        def getRuleIndex(self):
            return NodeTemplateParser.RULE_netConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNetConstant" ):
                listener.enterNetConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNetConstant" ):
                listener.exitNetConstant(self)




    def netConstant(self):

        localctx = NodeTemplateParser.NetConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_netConstant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(NodeTemplateParser.T__6)
            self.state = 101
            self.match(NodeTemplateParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EcuConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(NodeTemplateParser.NAME, 0)

        def getRuleIndex(self):
            return NodeTemplateParser.RULE_ecuConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEcuConstant" ):
                listener.enterEcuConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEcuConstant" ):
                listener.exitEcuConstant(self)




    def ecuConstant(self):

        localctx = NodeTemplateParser.EcuConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ecuConstant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(NodeTemplateParser.T__6)
            self.state = 104
            self.match(NodeTemplateParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





