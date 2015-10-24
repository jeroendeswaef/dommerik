import sys
import types
import uuid

from antlr4 import *

from CJSONLexer import CJSONLexer
from CJSONParser import CJSONParser
from CJSONListener import CJSONListener

from jinja2 import Template

class MyEmitter(CJSONListener):
    def __init__(self):
        self.currentObjUuid = None
        self.parents = []

    def getId(self, uuid):
        return 'o' + uuid

    def enterAnObject(self, ctx: CJSONParser.AnObjectContext):
        parent = None
        if len(self.parents) > 0:
            parent = self.parents[-1]
            if parent != None:
                parent = self.getId(parent)

        #print("enter obj", "parent: ", parent)
        objUuid = str(uuid.uuid4()).split('-')[0]
        objVar = self.getId(objUuid);
        #print(objUuid)
        self.currentObjUuid = objUuid;
        items = []
        for attrItem in ctx.pair():
            item = {
                'name': str(attrItem.STRING()).replace('\"',''),
                'value': str(attrItem.value().STRING()).replace('\"','')
            }
            items.append(item)
        with open('element_template.jinja') as txt:
            template = Template(txt.read())
            print(template.render(attrs=items, objVar=objVar, parentUuid=parent))

    def enterArrayOfValues(self, ctx: CJSONParser.ArrayOfValuesContext):
        #print("enter arr", len(ctx.value()))
        self.parents.append(self.currentObjUuid)

    def exitArrayOfValues(self, ctx: CJSONParser.ArrayOfValuesContext):
        self.parents.pop()

def main(argv):
    input = FileStream(argv[1])
    lexer = CJSONLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CJSONParser(stream)
    tree = parser.json()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    listener = MyEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    #template = Template('Hello {{ name }}!')
    #print(template.render(name='John Doe'))

if __name__ == '__main__':

    main(sys.argv)
