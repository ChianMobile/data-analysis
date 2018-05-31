
#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import os
import gzip
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
    if os.path.exists(path):
        gz_fileName = list()
        for root, dirs, files in os.walk(path):
            for gzfile in files:
                if os.path.splitext(gzfile)[1] == '.gz':
                    gz_fileName.append(gzfile)
    return gz_fileName

def get_file_line(paths,inpath,outpath):

    try:
        for gzfilenames in paths:

            outputfile_neigh = gzfilenames.split('.')[0] + '_neigh.csv'
            gzfile = file(os.path.join(outpath, outputfile_neigh), 'a')
            gzfile.write(
                'timestamp,deviceid,boottime,runingtime,wlanneighbornumber,wlanneighborradiotype,wlanneighborssidname,wlanneighbormac,wlanneighborchannel\r')
            con = read_gz_file(os.path.join(inpath, gzfilenames))
            if getattr(con, '__iter__', None):
                for line in con:
                    sa = line.split('|')
                    pattern = '^\d{1,3}$'
                    p1 = re.compile(pattern)
                    isnum = p1.match(sa[42])
                    if isnum and len(sa) >= (41+4*int(sa[41])) and int(sa[42]) > 0:
                        if sa[42] != '' and sa[42] >= '1':
                            for i in range(int(sa[42])):
                                gzfile.write(
                                    sa[0] + ',' + sa[4] + ',' + sa[22] + ',' + sa[23] +',' + sa[42] + ',' + sa[43 + i * 4] + \
                                    ',' + sa[44 + i * 4] + ',' + sa[45+ i * 4] + ',' + sa[46 + i * 4] + '\r')
                                gzfile.flush()


            gzfile.close()

    except IOError:
        print 'ERROR'
    finally:
        print 'AAAA'

if __name__ == '__main__':

    inpath = r'G:\MobileData\file\HGUINFO_0528'
    outpath = r'G:\MobileData\file\outfile'
    paths = get_gz_fileName(inpath)
    get_file_line(paths, inpath, outpath)

    print 'success'




























