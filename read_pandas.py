#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt
import matplotlib as mpl

import pandas as pd
import numpy as np


from pandas import Series,DataFrame



fd = open(r'C:\Users\Administrator\Desktop\������ �� ��������̽��˫��ƽ̨�澯�쳣�ձ�20180525.xlsx','rb')


fdata = pd.read_excel(fd, sheet_name=0)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


data = fdata[[u'����',u'����',u'���շ�',u'�澯������IP']]
'''
df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df.plot.bar()
'''



plt.figure(u'����')
#plt.plot(x, y_data)
city_num = data[u'����'].value_counts()
cfig = city_num.plot(kind='bar').get_figure()
plt.figure(u'����')
fun_num = data[u'����'].value_counts()
funfig = fun_num.plot(kind='bar').get_figure()
plt.figure(u'���շ�')
play_num = data[u'���շ�'].value_counts()
playfig = play_num.plot(kind='bar').get_figure()
plt.figure(u'�澯������IP')
ip_num = data[u'�澯������IP'].value_counts()
iphead = ip_num.head(10)
ipfig = iphead.plot(kind='bar').get_figure()

#cfig = city_num.plot(kind='bar').get_figure()
#funfig = fun_num.plot(kind='bar').get_figure()
#playfig = play_num.plot(kind='bar').get_figure()
#ipfig = ip_num.plot(kind='bar').get_figure()


cfig.savefig('city')
funfig.savefig('fun')
playfig.savefig('play')
ipfig.savefig('ip')
#print city_num
plt.show()


