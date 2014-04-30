#!/usr/bin/python
import os
import sys

CODE_PATH = '/build/trees/vdnet/main/automation/'

class codeConverter(object):
   def __init__(self): 
      self.anchorInfo = dict()

   def anchorBuilder(self, codepath, anchorinfo = {}):
      self.codePath = codepath
      for key in anchorinfo.keys():
	 newkey = key.replace('::','/')
	 newkey = newkey + '.pm'
	 newkey = os.path.join(CODE_PATH,newkey)
	 self.anchorInfo[newkey] = anchorinfo[key]

   def getAnchorInfo(self):
      return self.anchorInfo

   def convertCode(self):
      for key in self.anchorInfo.keys():
	 print "code path:  " + key
	 if os.path.exists(key):
	    if os.path.isfile(key):
	       self.readAndMark(key,self.anchorInfo[key])
	 else:
	    print '%s is not exist'%key

   def readAndMark(self,codepath,linenums):
      self.pos = 1
      parts = codepath.split('/')
      parts = parts[-1].split('.')
      outpath = os.path.join('.',parts[0]+'.html')
#      outpath = os.path.join('.','1.html')
     
      #print 'outpath' + outpath

      out = open(outpath,'wt')
      out.write('<html>')
      out.write('<body>')
      #print "linenums"
      #print linenums.count('1')
      for eachline in open(codepath, 'r'):
         if linenums.count(str(self.pos)) > 0:
       #out.write('<div id="%s" style="display:none;">here</div>\n' % self.pos)
	    out.write('<div id="%s"></div>\n' % self.pos)
	 eachline = '<fond>%d   %s</fond><br/>' % (self.pos,eachline)
	 out.write(eachline)
	 self.pos = self.pos + 1
      out.write('</body>')
      out.write('</html>')
      out.close()



	 
	 
