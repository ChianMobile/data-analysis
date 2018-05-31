#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import re
pattern = '\d+'
pattern = '^\d{1,}$'
p1 = re.compile(pattern)
number = p1.match('1!34')
if number:
   print "yes"
else:
   print "no"

#http://10.1.68.22/main.jsp