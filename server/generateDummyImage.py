# [width] [height] [name] [color]

import cv2
import numpy as np

name = 'dummy'
width = 200
height = 100

blank = np.zeros((height, width, 3))
blank += [200, 200, 200][::-1] # カラーコードを指定

cv2.imwrite(name + '-' + str(width) + 'x' + str(height) + '.png', blank)