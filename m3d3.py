#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt

import numpy as np

# ��ȡһ��С�׹�����Ƭ����ʾ
plt.figure('QinYeHong')
QinYeHong = plt.imread('dota2.png')
plt.imshow(QinYeHong)
plt.show()

