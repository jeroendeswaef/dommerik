# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .CJSONListener import CJSONListener
else:
    from CJSONListener import CJSONListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\16")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\5\2")
        buf.write("\17\n\2\3\3\3\3\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\7\5(\n\5\f\5\16\5+\13\5\3\5\3\5\3\5\3\5\5\5\61\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6:\n\6\3\6\2\2\7\2\4")
        buf.write("\6\b\n\2\2A\2\16\3\2\2\2\4\35\3\2\2\2\6\37\3\2\2\2\b\60")
        buf.write("\3\2\2\2\n9\3\2\2\2\f\17\5\4\3\2\r\17\5\b\5\2\16\f\3\2")
        buf.write("\2\2\16\r\3\2\2\2\17\3\3\2\2\2\20\21\7\3\2\2\21\26\5\6")
        buf.write("\4\2\22\23\7\4\2\2\23\25\5\6\4\2\24\22\3\2\2\2\25\30\3")
        buf.write("\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\31\3\2\2\2\30\26")
        buf.write("\3\2\2\2\31\32\7\5\2\2\32\36\3\2\2\2\33\34\7\3\2\2\34")
        buf.write("\36\7\5\2\2\35\20\3\2\2\2\35\33\3\2\2\2\36\5\3\2\2\2\37")
        buf.write(" \7\f\2\2 !\7\6\2\2!\"\5\n\6\2\"\7\3\2\2\2#$\7\7\2\2$")
        buf.write(")\5\n\6\2%&\7\4\2\2&(\5\n\6\2\'%\3\2\2\2(+\3\2\2\2)\'")
        buf.write("\3\2\2\2)*\3\2\2\2*,\3\2\2\2+)\3\2\2\2,-\7\b\2\2-\61\3")
        buf.write("\2\2\2./\7\7\2\2/\61\7\b\2\2\60#\3\2\2\2\60.\3\2\2\2\61")
        buf.write("\t\3\2\2\2\62:\7\f\2\2\63:\7\r\2\2\64:\5\4\3\2\65:\5\b")
        buf.write("\5\2\66:\7\t\2\2\67:\7\n\2\28:\7\13\2\29\62\3\2\2\29\63")
        buf.write("\3\2\2\29\64\3\2\2\29\65\3\2\2\29\66\3\2\2\29\67\3\2\2")
        buf.write("\298\3\2\2\2:\13\3\2\2\2\b\16\26\35)\609")
        return buf.getvalue()


class CJSONParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"','", u"'}'", u"':'", u"'['", 
                     u"']'", u"'true'", u"'false'", u"'null'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"STRING", u"NUMBER", 
                      u"WS" ]

    RULE_json = 0
    RULE_myobject = 1
    RULE_pair = 2
    RULE_array = 3
    RULE_value = 4

    ruleNames =  [ "json", "myobject", "pair", "array", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    STRING=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class JsonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def myobject(self):
            return self.getTypedRuleContext(CJSONParser.MyobjectContext,0)


        def array(self):
            return self.getTypedRuleContext(CJSONParser.ArrayContext,0)


        def getRuleIndex(self):
            return CJSONParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.exitJson(self)




    def json(self):

        localctx = CJSONParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.state = 12
            token = self._input.LA(1)
            if token in [CJSONParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.myobject()

            elif token in [CJSONParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.array()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MyobjectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CJSONParser.RULE_myobject

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnObjectContext(MyobjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CJSONParser.MyobjectContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CJSONParser.PairContext)
            else:
                return self.getTypedRuleContext(CJSONParser.PairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.enterAnObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.exitAnObject(self)


    class EmptyObjectContext(MyobjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CJSONParser.MyobjectContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.enterEmptyObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.exitEmptyObject(self)



    def myobject(self):

        localctx = CJSONParser.MyobjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_myobject)
        self._la = 0 # Token type
        try:
            self.state = 27
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = CJSONParser.AnObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(CJSONParser.T__0)
                self.state = 15
                self.pair()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CJSONParser.T__1:
                    self.state = 16
                    self.match(CJSONParser.T__1)
                    self.state = 17
                    self.pair()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 23
                self.match(CJSONParser.T__2)
                pass

            elif la_ == 2:
                localctx = CJSONParser.EmptyObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(CJSONParser.T__0)
                self.state = 26
                self.match(CJSONParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CJSONParser.STRING, 0)

        def value(self):
            return self.getTypedRuleContext(CJSONParser.ValueContext,0)


        def getRuleIndex(self):
            return CJSONParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.exitPair(self)




    def pair(self):

        localctx = CJSONParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(CJSONParser.STRING)
            self.state = 30
            self.match(CJSONParser.T__3)
            self.state = 31
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CJSONParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayOfValuesContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CJSONParser.ArrayContext)
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CJSONParser.ValueContext)
            else:
                return self.getTypedRuleContext(CJSONParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.enterArrayOfValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.exitArrayOfValues(self)


    class EmptyArrayContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CJSONParser.ArrayContext)
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.enterEmptyArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.exitEmptyArray(self)



    def array(self):

        localctx = CJSONParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 46
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = CJSONParser.ArrayOfValuesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(CJSONParser.T__4)
                self.state = 34
                self.value()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CJSONParser.T__1:
                    self.state = 35
                    self.match(CJSONParser.T__1)
                    self.state = 36
                    self.value()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.match(CJSONParser.T__5)
                pass

            elif la_ == 2:
                localctx = CJSONParser.EmptyArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(CJSONParser.T__4)
                self.state = 45
                self.match(CJSONParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CJSONParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(CJSONParser.NUMBER, 0)

        def myobject(self):
            return self.getTypedRuleContext(CJSONParser.MyobjectContext,0)


        def array(self):
            return self.getTypedRuleContext(CJSONParser.ArrayContext,0)


        def getRuleIndex(self):
            return CJSONParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, CJSONListener ):
                listener.exitValue(self)




    def value(self):

        localctx = CJSONParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 55
            token = self._input.LA(1)
            if token in [CJSONParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(CJSONParser.STRING)

            elif token in [CJSONParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(CJSONParser.NUMBER)

            elif token in [CJSONParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.myobject()

            elif token in [CJSONParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.array()

            elif token in [CJSONParser.T__6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.match(CJSONParser.T__6)

            elif token in [CJSONParser.T__7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.match(CJSONParser.T__7)

            elif token in [CJSONParser.T__8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.match(CJSONParser.T__8)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




