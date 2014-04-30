#!/usr/bin/python
from convert import *
from htmlclass import *
from codeConverter import *

LOGPATH = '../log/9969vdnet(1).log'
#LOGPATH = './test.log'
CODE_PATH = '/build/trees/vdnet/main/automation/main/'


def main():
   filereader = FileReader(LOGPATH)
   filedata = filereader.substitution()
   cc = codeConverter()
   anchorinfo = filereader.getAnchorInfo()
   cc.anchorBuilder(CODE_PATH,anchorinfo)
   print "code anchorinfo: "
   print cc.getAnchorInfo()
   cc.convertCode()
   hm = htmlMaker(filedata,'./testoutput.html')
   hm.produceHtml()

if __name__ == '__main__':
   main()
