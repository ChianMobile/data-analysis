#-*- coding: gbk -*-
# encoding =gbk
import sys
#sys.setdefaultencoding('utf-8')
if sys.getdefaultencoding() != 'gbk':
   reload(sys)
   sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)

# ��������500
n_samples = 500
dim = 3

# ������һ��3ά��̬�ֲ����ݣ����ݷ�����ȫ���
samples = np.random.multivariate_normal(
    np.zeros(dim),
    np.eye(dim),
    n_samples
)

# ͨ����ÿ��������ԭ�����;��ȷֲ��Ǻϵõ������ھ��ȷֲ�������
for i in range(samples.shape[0]):
    r = np.power(np.random.random(), 1.0/ 3.0)
    samples[i] *= r / np.linalg.norm(samples[i])

upper_samples = []
lower_samples = []

for x, y, z in samples:
    # 3x+2y-z=1��Ϊ�б�ƽ��
    if z > 3 * x + 2 * y - 1:
        upper_samples.append((x, y, z))
    else:
        lower_samples.append((x, y, z))

fig = plt.figure('3D scatter plot')
ax = fig.add_subplot(111, projection='3d')

uppers = np.array(upper_samples)
lowers = np.array(lower_samples)

# �ò�ͬ��ɫ��ͬ��״��ͼ���ʾƽ�����µ�����
# �б�ƽ���ϰ벿��Ϊ��ɫԲ�㣬�°벿��Ϊ��ɫ����
ax.scatter(uppers[:, 0], uppers[:, 1], uppers[:, 2], c='r', marker='o')
ax.scatter(lowers[:, 0], lowers[:, 1], lowers[:, 2], c='g', marker='^')

plt.show()