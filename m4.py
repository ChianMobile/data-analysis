#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-5,5,20)
fig, ax = plt.subplots()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))   # set position of y spine to y=0



#ax.plot(x, x+0, color="red", alpha=0.5) # half-transparant red
#ax.plot(x, x+1, color="#1155dd")        # RGB hex code for a bluish color
#ax.plot(x, x+2, color="#15cc55")
#linewidth 或是 lw 参数改变线宽。 linestyle 或是 ls 参数改变线的风格。
#ax.plot(x, x+5, color="red", lw=2, linestyle='-')
ax.plot(x, x**3, color="red", lw=2, ls='-.')

ax.plot(x, x**2+3*x+2, color="red", lw=2, ls=':')

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...

ax.xaxis.labelpad = 5





plt.show()