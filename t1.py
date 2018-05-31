import time
import math
import numpy as np
x = [i * 0.001 for i in xrange(10)]
#print x
start = time.clock()
#print start
for i, t in enumerate(x):

 print i,t
 x[i] = math.sin(t)
print "math.sin:", time.clock() - start
x = [i * 0.001 for i in xrange(10)]
x = np.array(x)
start = time.clock()
np.sin(x,x)
print "numpy.sin:", time.clock() - start
print time.strftime("%Y%m%d %H%M%S", time.localtime())
print type(time.clock())
print type( time.localtime())
print type(time.time())
#print time.localtime(time.time())
print time.asctime( time.localtime(time.time()) )