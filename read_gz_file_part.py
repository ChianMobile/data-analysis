
#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import gzip


def read_gz_file(path):
    if os.path.exists(path):
        with gzip.open(path, 'rb') as pf:
            for line in pf:
                yield line
    else:
        print('the path [{}] is not exist!'.format(path))
def get_gz_fileName(path):
    gz_fileName = list()
    for root, dirs, files in os.walk(path):
        for gzfile in files:
            if os.path.splitext(gzfile)[1] == '.gz':
                gz_fileName.append(gzfile)
    return gz_fileName

def get_file_line(paths):

    try:
        global wan
        gzfile = file(r'G:\MobileData\gzfile.csv','a')
        #gzfile.write('deviceid|wanindex|wanname|wanavertxrate|wanaverrxrate|wanmaxtxrate|wanmaxrxrate')
        gzfile.write('timestamp,deviceid,wanindex,wanavertxrate,wanaverrxrate,wanmaxtxrate,wanmaxrxrate\r\n')

        for path in paths:
            con = read_gz_file(os.path.join(r'G:\MobileData\chen', path))
            if getattr(con, '__iter__', None):
                for line in con:
                    # print line
                    sa = line.split('|')
                    #print sa
                    if sa[21] != '':
                        #print len(sa)
                        index_a = 21 + int(sa[21]) * 6 + 2

                        # print 'ec', sa[21] subdevice
                        wan = sa[0] + ',' + sa[4] + ','
                        for i in range(int(sa[21])):
                            wan = wan + sa[22 + i * 6]+','+sa[24 + i * 6]+','+sa[25 + i * 6]+','+sa[26 + i * 6]+','+sa[27 + i * 6]+ ','
                            #print sa[0],sa[4],sa[22 + i * 6], sa[23 + i * 6], sa[24 + i * 6], sa[25 + i * 6], sa[26 + i * 6], sa[27 + i * 6]
                            #wan = sa[0]+','+sa[4]+','+sa[22 + i * 6]+','+sa[24 + i * 6]+','+sa[25 + i * 6]+','+sa[26 + i * 6]+','+sa[27 + i * 6]
                            #print wan
                            #gzfile.write(sa[0]+','+sa[4]+','+sa[22 + i * 6]+','+sa[24 + i * 6]+','+sa[25 + i * 6]+','+sa[26 + i * 6]+','+sa[27 + i * 6]+'\r\n')
                            #gzfile.flush()
                        #print wan
                    #index_a = 21+int(sa[21])*6+2
                    #print index_a
                    #print 21+int(sa[21])*6+2

                    if len(sa) >= index_a and sa[index_a] != '':
                        #pass
                        #print sa[index_a]
                        for i in range(int(sa[index_a])):
                            if i == 1:

                                #print wan
                                lan = sa[4] +','+  sa[int(index_a) + 6 + i * 13] + ',' + sa[int(index_a) + 7 + i * 13] + ',' + sa[int(index_a) + 12 + i * 13] + ',' + sa[int(index_a) + 13 + i * 13]
                                print lan
                                wan = wan + sa[int(index_a) + 6 + i * 13] + ',' + sa[int(index_a) + 7 + i * 13] + ',' + sa[int(index_a) + 12 + i * 13] + ',' + sa[int(index_a) + 13 + i * 13] + '\r\n'
                                #print wan
                                #gzfile.write(wan)
                                #gzfile.flush()


                            else:
                                continue
                            #lan = wan + sa[int(index_a) + i * 13] + ',' + sa[int(index_a) + i * 13] + ',' + sa[int(index_a) + i * 13] + ',' + sa[int(index_a) + i * 13] + ','


        #gzfile.close()




    except IOError:

        print 'BBBB'
    finally:
        print 'AAAA'

if __name__=='__main__':

    paths = get_gz_fileName(r'G:\MobileData\chen')
    get_file_line(paths)





