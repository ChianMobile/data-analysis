#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt
import numpy as np

# 3Dͼ������ģ�飬project='3d'�Ķ���
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)

n_grids = 51        	# x-yƽ��ĸ����
c = n_grids / 2     	# ����λ��
nf = 2              	# ��Ƶ�ɷֵĸ���

# ���ɸ��
x = np.linspace(0, 1, n_grids)
y = np.linspace(0, 1, n_grids)

# x��y�ǳ���Ϊn_grids��array
# meshgrid���x��y��ϳ�n_grids*n_grids��array��X��Y��Ӧλ�þ������и�������
X, Y = np.meshgrid(x, y)

# ����һ��0ֵ�ĸ���Ҷ��
spectrum = np.zeros((n_grids, n_grids), dtype=np.complex)

# ����һ��������������(2*nf+1)**2/2
noise = [np.complex(x, y) for x, y in np.random.uniform(-1 ,1 ,(( 2 * nf +1 ) ** 2 /2, 2))]

# ����ҶƵ�׵�ÿһ����乲��������ĶԳ�
noisy_block = np.concatenate((noise, [0j], np.conjugate(noise[::-1])))

# �����ɵ�Ƶ����Ϊ��Ƶ�ɷ�
spectrum[ c -nf: c + nf +1, c- nf:c + nf + 1] = noisy_block.reshape((2 * nf + 1, 2 * nf + 1))

# ���з�����Ҷ�任
Z = np.real(np.fft.ifft2(np.fft.ifftshift(spectrum)))

# ����ͼ��
fig = plt.figure('3D surface & wire')

# ��һ����ͼ��surfaceͼ
ax = fig.add_subplot(1, 2, 1, projection='3d')

# alpha����͸���ȣ�cmap��color map
# rstride��cstride�����������ϵĲ�����ԽСԽ��ϸ��lw���߿�
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='jet', rstride=1, cstride=1, lw=0)

# �ڶ�����ͼ������ͼ
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3, lw=0.5)

plt.show()