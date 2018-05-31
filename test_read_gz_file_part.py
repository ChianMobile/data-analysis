
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

        gzfile = file(r'G:\MobileData\gzfile.csv','a')
        #gzfile.write('deviceid|wanindex|wanname|wanavertxrate|wanaverrxrate|wanmaxtxrate|wanmaxrxrate')
        gzfile.write('timestamp,deviceid,wanindex,wanavertxrate,wanaverrxrate,wanmaxtxrate,wanmaxrxrate\r\n')
        subdevice = file(r'G:\MobileData\subdevice.csv','a')
        subdevice.write('deviceid,subdeviceavertxrate,subdeviceaverrxrate,lanupstatistics,landownstatistics\r\n')



        for path in paths:
            con = read_gz_file(os.path.join(r'G:\MobileData\chen', path))
            if getattr(con, '__iter__', None):
                for line in con:
                    sa = line.split('|')
                    if sa[21] != '':
                        index_a = 21 + int(sa[21]) * 6 + 2

                        # print 'ec', sa[21] subdevice
                        for i in range(int(sa[21])):
                            #wan = wan + sa[22 + i * 6]+','+sa[24 + i * 6]+','+sa[25 + i * 6]+','+sa[26 + i * 6]+','+sa[27 + i * 6]+ ','
                            #print sa[0],sa[4],sa[22 + i * 6], sa[23 + i * 6], sa[24 + i * 6], sa[25 + i * 6], sa[26 + i * 6], sa[27 + i * 6]
                            #wan = sa[0]+','+sa[4]+','+sa[22 + i * 6]+','+sa[24 + i * 6]+','+sa[25 + i * 6]+','+sa[26 + i * 6]+','+sa[27 + i * 6]
                            #print 1
                            gzfile.write(sa[0]+','+sa[4]+','+sa[22 + i * 6]+','+sa[24 + i * 6]+','+sa[25 + i * 6]+','+sa[26 + i * 6]+','+sa[27 + i * 6]+'\r\n')
                            gzfile.flush()

                        if sa[index_a] == '1':
                            if len(sa) >= index_a + 11:

                                i = 0
                                #lan = sa[4] + ',' + sa[int(index_a) + 6 + i * 11] + ',' + sa[int(index_a) + 7 + i * 11] + ',' + sa[int(index_a) + 10 + i * 11] + ',' + sa[int(index_a) + 11 + i * 11]
                                lan = sa[4] + ',' + sa[int(index_a) + 6 + i * 11] + ',' + sa[int(index_a) + 7 + i * 11]
                                print lan
                                subdevice.write(lan+'\r\n')
                                subdevice.flush()
                        elif sa[index_a] >= '1' and sa[index_a] != '':
                            for i in range(int(sa[index_a])):
                                if len(sa) >= index_a + 13 * i:
                                    lan = sa[4] + ',' + sa[int(index_a) + 6 + i * 11] + ',' + sa[int(index_a) + 7 + i * 11]

                                    print lan
                                    subdevice.write(lan+'\r\n')
                                    subdevice.flush()











        gzfile.close()
        subdevice.close()




    except IOError:

        print 'BBBB'
    finally:
        print 'AAAA'

if __name__=='__main__':

    paths = get_gz_fileName(r'G:\MobileData\chen')
    get_file_line(paths)





