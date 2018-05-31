#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt

import numpy as np

# 读取一张小白狗的照片并显示
plt.figure('QinYeHong')
QinYeHong = plt.imread('dota2.png')
plt.imshow(QinYeHong)
plt.show()

