#-*- coding: gbk -*-
# encoding =gbk
import numpy as np

speed_map = {
    'dog': (48, '#7199cf'),
    'cat': (45, '#4fc4aa'),
    'cheetah': (120, '#e1a7a2')
}
#print speed_map.keys()
speeds = [x[0] for x in speed_map.values()]
print speeds
animals = speed_map.keys()
print animals
labels = ['{}\n{} km/h'.format(animal, speed) for animal, speed in zip(animals, speeds)]

xticks = np.arange(3)
#print xticks
a=['{}\n{} km/h'.format(animals,speeds,) for animal, speed in zip(animals, speeds)]
#print labels
for animal, speed in zip(animals, speeds):
    print '{}\n{} km/h'.format(animal, speed)