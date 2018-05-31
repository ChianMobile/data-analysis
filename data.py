#-*- coding: gbk -*-

import pandas as pd
import numpy as np
import vtk
#import mayavi.mlab
#from mayavi import mlab

from pandas import Series,DataFrame
#f = open(r'C:\Users\Administrator\Desktop\go\公司12月份通讯录.xlsx','rb')
#df = pd.read_excel(open(r'C:\Users\Administrator\Desktop\go\公司12月份通讯录.xlsx','rb'),sheet_name = 'Sheet2')
#print df.apply(pd.Series.value_counts)
#df[[col1, col2]]
#data = df[[u'姓名', u'职务', u'手机号码', u'邮箱']]
#print pd.notnull(data)
#print data.fillna('XXX')

#g = data.groupby([u'姓名'])
#df.pivot_table(index=col1, values=[col2,col3], aggfunc=max)：创建一个按列col1进行分组，并计算col2和col3的最大值的数据透视表

#dp = data.pivot_table(index=u'姓名', values=[u'手机号码',u'邮箱'], aggfunc=max)
#print data.describe()
#print data.max()
#s = pd.Series([1,3,5,np.nan,6,8])
s = pd.Series(data=[1,2,3,4],index = ['a','b','c','d'])
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),  # //生成Series对象,取的是value
                     'D' : np.array([3] * 4,dtype='int32'),  #//生成numpy对象
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
#print pd.Series(1,index=list(range(4)),dtype='float32')
a = np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])

#print np.random.randint(5,10,size = (5,10))
#print a[0,3:5]
#print a[:,2]
#print  np.add.reduce([[1,2,3],[4,5,6]], axis=1)
x = np.array([[1,2],
              [3,4],
              [5,6]])
print x.T























#df1=pd.DataFrame(df)
#print df1
#print df
#import cv2


# or using sheet index starting 0
#df = pd.read_excel(open(r'C:\Users\Administrator\Desktop\go\公司12月份通讯录.xlsx','rb'), sheetname=2)


#data = pd.read_excel(r'C:\Users\Administrator\Desktop\go\公司12月份通讯录.xlsx', sheetname=0)
'''test'''

s = '2016-10-13192307|V1.0.0|0572|00420100060200601611002468D6DF74|\
||0|0|0||1463587138043|61710|6451784|1583|0|41833|113000|6000|0|9053164.00|\
9286957.00|8117642.00|0.00|0.00|||||||||||||||||||||||3|9|13||112.17.8.10|\
1|0|0|0||0|9|13|9|9|13|1|0|10|11||112.17.8.5|1|0|0|0||0|10|11|10|10|11|1|0|7|18|\
|112.17.8.78|1|0|0|0||0|7|18|7|7|18|1|0|1|9|9053164.00||11||112.17.8.78|\
27|13|9286957.00|15|6|8117642.00|256|313|27|0|27|0|0||0|1|1|1|2194|0|67791699|27|6451784'
ss = s.split('|')
#print ss.count('')
for i in ss:
    if i != '':
        #print i
        pass


