#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-np.pi,np.pi,0.01)
y=np.sin(x)
#print y
plt.plot(x,y,'g')
plt.show()