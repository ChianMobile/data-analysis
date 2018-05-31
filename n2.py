#-*- coding: gbk -*-
import sys
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame(np.random.randn(1000, 4), columns=list("ABCD"))
#print np.random.randn(1000, 4)
#print np.random.rand(6, 4)
df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df.plot.bar()
print df
plt.show()

