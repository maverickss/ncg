#!/usr/bin/python
#
#    Html class for python
#

class htmlMaker(object):
   def __init__(self, bodyData, Output):
      self.bodyData = bodyData
      self.Output = Output

   def produceHtml(self):
      title = 'Log Viewer'
      self.title = '<title>%s</title>\n' % title
      self.body = '<body>\n%s</body>\n' % self.bodyData
      filehandler = open(self.Output, 'w')
      filehandler.write('<!DOCTYPE html>\n')
      filehandler.write('<html>\n')
      filehandler.write(self.title)
      filehandler.write(self.body)
      filehandler.write('</html>\n')
      filehandler.close()

if __name__ == '__main__':
   hm = htmlMaker("sdfasdf\nsdfdf",'./testoutput.html')
   hm.produceHtml()




