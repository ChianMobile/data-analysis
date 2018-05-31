#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt
import numpy as np
try:

    files = file(r'G:\MobileData\chen\HGUPERIODIC_20180417000855_15_075_2071\HGUPERIODIC_20180417000855_15_075_2071','r')
    l = 0
    for line in files:
        l = l+1
        print l
        sa = line.split('|')
        print sa
        if sa[21] !='':
            index_a = 21 + int(sa[21]) * 6 + 2
            print 'ec',sa[21]
            for i in range(int(sa[21])):
                pass
                #print sa[22+i*6], sa[23+i*6], sa[24+i*6], sa[25+i*6], sa[26+i*6], sa[27+i*6]
            if len(sa) >= index_a+13:
                print len(sa)
                print index_a

                i = 0
                lan = sa[4] + ',' + sa[int(index_a) + 6 + i * 13] + ',' + sa[int(index_a) + 7 + i * 13] + ',' + sa[int(index_a) + 12 + i * 13] + ',' + sa[int(index_a) + 13 + i * 13]
                print lan
            else:
                continue

except IOError:
    print '0000'
#s = fs.readline()
#ss = s.split('|')
#print ss
#print ss[21]
#for i in range(int(ss[21])):
    #print ss[22+(i-1)*6], ss[23+(i-1)*6], ss[24+(i-1)*6], ss[25+(i-1)*6], ss[26+(i-1)*6], ss[27+(i-1)*6]
#print ss[22],ss[23],ss[24],ss[25],ss[26],ss[27]
#for i in range(int(ss[21])):
    #print ss[22+i*6], ss[23+i*6], ss[24+i*6], ss[25+i*6], ss[26+i*6], ss[27+i*6]