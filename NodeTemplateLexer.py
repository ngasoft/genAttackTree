# Generated from C:/Users/ac1222/OneDrive - Coventry University/GitHub/genAT\NodeTemplate.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\7\17K\n\17\f")
        buf.write("\17\16\17N\13\17\3\20\3\20\3\20\3\21\6\21T\n\21\r\21\16")
        buf.write("\21U\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\5\4")
        buf.write("\2C\\c|\5\2\62;C\\c|\5\2\13\f\17\17\"\"\2Z\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'")
        buf.write("\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17/\3\2\2\2")
        buf.write("\21\61\3\2\2\2\23\65\3\2\2\2\258\3\2\2\2\27=\3\2\2\2\31")
        buf.write("A\3\2\2\2\33E\3\2\2\2\35H\3\2\2\2\37O\3\2\2\2!S\3\2\2")
        buf.write("\2#$\7<\2\2$\4\3\2\2\2%&\7%\2\2&\6\3\2\2\2\'(\7\61\2\2")
        buf.write("(\b\3\2\2\2)*\7B\2\2*\n\3\2\2\2+,\7]\2\2,\f\3\2\2\2-.")
        buf.write("\7_\2\2.\16\3\2\2\2/\60\7~\2\2\60\20\3\2\2\2\61\62\7C")
        buf.write("\2\2\62\63\7P\2\2\63\64\7F\2\2\64\22\3\2\2\2\65\66\7Q")
        buf.write("\2\2\66\67\7T\2\2\67\24\3\2\2\289\7U\2\29:\7C\2\2:;\7")
        buf.write("P\2\2;<\7F\2\2<\26\3\2\2\2=>\7P\2\2>?\7G\2\2?@\7V\2\2")
        buf.write("@\30\3\2\2\2AB\7G\2\2BC\7E\2\2CD\7W\2\2D\32\3\2\2\2EF")
        buf.write("\7C\2\2FG\7R\2\2G\34\3\2\2\2HL\t\2\2\2IK\t\3\2\2JI\3\2")
        buf.write("\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\36\3\2\2\2NL\3\2\2")
        buf.write("\2OP\7\60\2\2PQ\7\60\2\2Q \3\2\2\2RT\t\4\2\2SR\3\2\2\2")
        buf.write("TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VW\3\2\2\2WX\b\21\2\2X\"")
        buf.write("\3\2\2\2\5\2LU\3\b\2\2")
        return buf.getvalue()


class NodeTemplateLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    AND = 8
    OR = 9
    SAND = 10
    NET = 11
    ECU = 12
    AP = 13
    NAME = 14
    DCOLON = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'#'", "'/'", "'@'", "'['", "']'", "'|'", "'AND'", "'OR'", 
            "'SAND'", "'NET'", "'ECU'", "'AP'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "SAND", "NET", "ECU", "AP", "NAME", "DCOLON", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "AND", "OR", "SAND", "NET", "ECU", "AP", "NAME", "DCOLON", 
                  "WS" ]

    grammarFileName = "NodeTemplate.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


