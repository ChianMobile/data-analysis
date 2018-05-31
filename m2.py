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

mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['ytick.major.size'] = 0

# �����˹���è���Ա�����߱����ٶȣ����ж�Ӧ�Ŀ��ӻ���ɫ
speed_map = {
    'dog': (48, '#7199cf'),
    'cat': (45, '#4fc4aa'),
    'cheetah': (120, '#e1a7a2')
}

# ����ͼ�ı���
fig = plt.figure('Bar chart & Pie chart')

# ������ͼ�ϼ���һ����ͼ��121����˼����һ��1��2�е���ͼ�еĵ�һ��
ax = fig.add_subplot(121)
ax.set_title('Running speed - bar chart')

# ����x��ÿ��Ԫ�ص�λ��
xticks = np.arange(3)

# ������״ͼÿ�����Ŀ��
bar_width = 0.5

# ��������
animals = speed_map.keys()

# �����ٶ�
speeds = [x[0] for x in speed_map.values()]

# ��Ӧ��ɫ
colors = [x[1] for x in speed_map.values()]

# ����״ͼ�������Ƕ����ǩ��λ�ã��������ٶȣ��������Ŀ�ȣ�ͬʱ�������ı�ԵΪ͸��
bars = ax.bar(xticks, speeds, width=bar_width, edgecolor='none')

# ����y��ı���
ax.set_ylabel('Speed(km/h)')

# x��ÿ����ǩ�ľ���λ�ã�����Ϊÿ����������
ax.set_xticks(xticks + bar_width / 2)

# ����ÿ����ǩ������
ax.set_xticklabels(animals)

# ����x��ķ�Χ
ax.set_xlim([bar_width / 2 - 0.5, 3 - bar_width / 2])

# ����y��ķ�Χ
ax.set_ylim([0, 125])

# ��ÿ��bar����ָ������ɫ
for bar, color in zip(bars, colors):
    bar.set_color(color)

# ��122λ�ü����µ�ͼ
ax = fig.add_subplot(122)
ax.set_title('Running speed - pie chart')

# ����ͬʱ�������ƺ��ٶȵı�ǩ
labels = ['{}\n{} km/h'.format(animal, speed) for animal, speed in zip(animals, speeds)]

# ����״ͼ����ָ����ǩ�Ͷ�Ӧ��ɫ
ax.pie(speeds, labels=labels, colors=colors)

plt.show()