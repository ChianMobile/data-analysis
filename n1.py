#-*- coding: gbk -*-
import numpy as np

a = [1, 2, 3, 4]  #
b = np.array(a)  # array([1, 2, 3, 4])
type(b)  # <type 'numpy.ndarray'>

b.shape  # (4,)
b.argmax()  # 3
b.max()  # 4
b.mean()  # 2.5

c = [[1, 2], [3, 4]]  # ��ά�б�
d = np.array(c)  # ��άnumpy����
d.shape  # (2, 2)
d.size  # 4
d.max(axis=0)  # ��ά��0��Ҳ�������һ��ά���ϵ����ֵ��array([3, 4])
d.max(axis=1)  # ��ά��1��Ҳ���ǵ����ڶ���ά���ϵ����ֵ��array([2, 4])
d.mean(axis=0)  # ��ά��0��Ҳ���ǵ�һ��ά���ϵľ�ֵ��array([ 2.,  3.])
d.flatten()  # չ��һ��numpy����Ϊ1ά���飬array([1, 2, 3, 4])
np.ravel(c)  # չ��һ�����Խ����ĽṹΪ1ά���飬array([1, 2, 3, 4])

# 3x3�ĸ�����2ά���飬���ҳ�ʼ������Ԫ��ֵΪ1
e = np.ones((3, 3), dtype=np.float)

# ����һ��һά���飬Ԫ��ֵ�ǰ�3�ظ�4�Σ�array([3, 3, 3, 3])
f = np.repeat(3, 4)

# 2x2x3���޷���8λ����3ά���飬���ҳ�ʼ������Ԫ��ֵΪ0
g = np.zeros((2, 2, 3), dtype=np.uint8)
g.shape  # (2, 2, 3)
h = g.astype(np.float)  # ����һ�����ͱ�ʾ

l = np.arange(10)  # ����range��array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
m = np.linspace(0, 6, 5)  # �Ȳ����У�0��6֮��5��ȡֵ��array([ 0., 1.5, 3., 4.5, 6.])

p = np.array(
    [[1, 2, 3, 4],
     [5, 6, 7, 8]]
)

np.save('p.npy', p)  # ���浽�ļ�
q = np.load('p.npy')  # ���ļ���ȡ