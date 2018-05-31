
#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import os
import gzip
import threading
import time
import re


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

def get_file_line(gzfilename,inpath,outpath):

    try:

        outputfile_neigh = gzfilename.split('.')[0]+'_neigh.csv'
        gzfile = file(os.path.join(outpath, outputfile_neigh), 'a')
        gzfile.write('timestamp,deviceid,boottime,runingtime,wlanneighbornumber,wlanneighborradiotype,wlanneighborssidname,wlanneighbormac,wlanneighborchannel\r')
        con = read_gz_file(os.path.join(inpath, gzfilename))
        if getattr(con, '__iter__', None):
            for line in con:
                sa = line.split('|')
                pattern = '^\d{1,3}$'
                p1 = re.compile(pattern)
                isnum = p1.match(sa[42])
                if isnum and len(sa) >= (41 + 4 * int(sa[41])) and int(sa[42]) > 0:
                    if sa[42] != '' and sa[42] >= '1':
                        for i in range(int(sa[42])):
                            gzfile.write(
                                sa[0] + ',' + sa[4] + ',' + sa[22] + ',' + sa[23] + ',' + sa[42] + ',' + sa[
                                    43 + i * 4] + \
                                ',' + sa[44 + i * 4] + ',' + sa[45 + i * 4] + ',' + sa[46 + i * 4] + '\r')
                            gzfile.flush()

        gzfile.close()


    except IOError:
        print 'IOERROR'
    finally:
        print 'AAAA'

if __name__ == '__main__':
    a = time.clock()
    inpath = r'G:\MobileData\file\HGUINFO_0528'
    outpath = r'G:\MobileData\file\outfile'
    thread_list = []
    paths = get_gz_fileName(inpath)
    for gzfilename in paths:
        t = threading.Thread(target=get_file_line, args=(gzfilename,inpath,outpath))
        t.start()

        thread_list.append(t)

    for t in thread_list:
        t.join()
    b = time.clock()
    print b-a
    print 'success'













