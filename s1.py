import os
import gzip
import threading
import time


def read_gz_file(path):
    if os.path.exists(path):
        with gzip.open(path, 'rb') as pf:
            for line in pf:
                #print line
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
paths = get_gz_fileName(r'G:\MobileData\chen')
for path in paths:

    con = read_gz_file(os.path.join(r'G:\MobileData\chen', path))
    for line in con:
        pass
        #print line
    if getattr(con, '__iter__', None):
        for line in con:
            pass
            #print line