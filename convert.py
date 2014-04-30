#!/usr/bin/python
import os
import sys
import re
from htmlclass import *

#Global variables
LOGPATH='./test.log'

class FileReader(object):
   def __init__(self, logPath):
      self.logPath = logPath
      if not os.path.exists(self.logPath):
	 print "%s do not exist" % self.logPath
      self.logData = open(self.logPath, 'r').read()
      self.fileData = ''
      self.anchorInfo = dict() 

    #  print self.logData

   def substitution(self):
      self.semicoloncount = 0
      self.colonid = 0
      pattern = r'\[ERROR\].*\[@(.+):(\d+)\]'
      semicolonpattern1 = r'\$VAR\d+\s*=\s*.*{'
      semicolonpattern2 = r'};'
#      pattern = r'\[ERROR\]'
      self.fileData = self.fileData + '<script type="text/javascript" src="click.js"></script>\n'
      for eachline in open(self.logPath, 'r'):
	 s = re.search(pattern, eachline)
	 if s:
	    #print s.group(1)
	    #print '*********'
	    self.addAnchorInfo(s.group(1),s.group(2))
	    parts = s.group(1).split('::')
	    parts = parts[-1].split(':')


	    def convertLinker(content):
	       result = '<a href = \"%s.html#%s\"> %s </a>' % (parts[0],content.group(2),content.group(0))
	       return result
	    rx = re.compile(pattern)
	    eachline = rx.sub(convertLinker,eachline)
            eachline = eachline.strip()
         #self.fileData = self.fileData+ ''.join('%s' % eachline+'<br>\n')

         #handle semicolon match
	 frontcolonlist = re.findall(semicolonpattern1,eachline);
	 for i in frontcolonlist:
	    writedata = "<div style=\"CURSOR: normal\" onclick=\"foldout('colon%d');\"></div>\n<a href=\"#\" onclick=\"foldout('colon%d');\">click</a><br>\n<div id='colon%d' style=\"display:block;\">\n" % (self.colonid,self.colonid,self.colonid)
	    self.colonid = self.colonid + 1
	    eachline = eachline.replace(i,str(i)+writedata)
	 lattercolonlist = re.findall(semicolonpattern2,eachline);
	 for j in lattercolonlist:
	    eachline = eachline.replace(j,'};</div>')
	 self.fileData = self.fileData + eachline
	 print len(frontcolonlist)+len(lattercolonlist)
	 if len(frontcolonlist) + len(lattercolonlist) == 0:
            self.fileData = self.fileData+ ''.join('%s' % eachline+'<br>\n')

      #print self.fileData
      return self.fileData

   def addAnchorInfo(self, key, value):
      if not self.anchorInfo.has_key(key):
	 realvalue = list()
      else:
	 realvalue = self.anchorInfo[key]
      if realvalue.count(value) == 0:
         realvalue.append(value)
         self.anchorInfo[key] = realvalue
   
   def getAnchorInfo(self):
      return self.anchorInfo

    


if __name__=='__main__':
   filedata = FileReader(LOGPATH)
   filedata.substitution()
   print filedata.getAnchorInfo()

