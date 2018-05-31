
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
        for path in paths:

            outputfile_wan = path.split('.')[0]+'_wan.csv'
            outputfile_lan = path.split('.')[0] + '_lan.csv'
            gzfile = file(os.path.join(outpath, outputfile_wan), 'a')
            gzfile.write('timestamp,deviceid,wanindex,wanname,wanavertxrate,wanaverrxrate,wanmaxtxrate,wanmaxrxrate\r')
            subdevice = file(os.path.join(outpath, outputfile_lan), 'a')
            subdevice.write('timestamp,deviceid,subdevicenumber,subdevicename,subdevicemac,subdeviceavertxrate,subdeviceaverrxrate,lanupstatistics,landownstatistics\r')
            con = read_gz_file(os.path.join(inpath, path))
            if getattr(con, '__iter__', None):
                for line in con:
                    sa = line.split('|')
                    if sa[21] != '':
                        index_a = 21 + int(sa[21]) * 6 + 2
                        for i in range(int(sa[21])):
                            gzfile.write(sa[0]+','+sa[4]+','+sa[22 + i * 6]+','+sa[23 + i * 6]+','+sa[24 + i * 6]+\
                                         ','+sa[25 + i * 6]+','+sa[26 + i * 6]+','+sa[27 + i * 6]+'\r')
                            gzfile.flush()
                        if sa[index_a] == '1':
                            if len(sa) >= index_a + 11:
                                i = 0
                                lan = sa[0]+',' + sa[4] + ',' + sa[index_a] + ',' + sa[int(index_a) + 2 + i * 11] + ',' + sa[int(index_a) + 5 + i * 11] +\
                                      ','+ sa[int(index_a) + 6 + i * 11] + ',' + sa[int(index_a) + 7 + i * 11]
                                #print lan
                                subdevice.write(lan+'\r')
                                subdevice.flush()
                        elif sa[index_a] >= '1' and sa[index_a] != '':
                            for i in range(int(sa[index_a])):
                                if len(sa) >= index_a + 13 * i:
                                    lan = sa[0]+',' + sa[4] + ',' + sa[index_a]  \
                                        + ',' + sa[int(index_a) + 2 + i * 11] + ',' + sa[int(index_a) + 5 + i * 11] +\
                                          ',' + sa[int(index_a) + 6 + i * 11] + ',' + sa[int(index_a) + 7 + i * 11]
                                    #print lan
                                    subdevice.write(lan+'\r')
                                    subdevice.flush()
            gzfile.close()
            subdevice.close()

    except IOError:
        print 'ERROR'
    finally:
        print 'AAAA'

if __name__ == '__main__':
    a = time.clock()
    inpath = r'G:\MobileData\temp'
    outpath = r'G:\MobileData\outFile'
    paths = get_gz_fileName(inpath)
    get_file_line(paths, inpath, outpath)
    b = time.clock()
    print b-a
    print 'success'




























