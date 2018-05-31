#-*- coding: gbk -*-

import pandas as pd
import numpy as np
from mayavi import mlab
from pandas import Series,DataFrame

#df = pd.read_csv(r'G:\MobileData\HGUPERIODIC_20180417000855_15_075_2071_lan.csv')
#for d in df['subdevicename']:
   # pass
    #print d
#df['subdevicename'].to_csv('abc.csv')
dic = {'a':1,'b':2,'c':3}
print dic
#p = pd.DataFrame(dic)


p = pd.DataFrame(np.random.rand(20,5))
print p