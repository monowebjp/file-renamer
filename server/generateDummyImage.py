# [width] [height] [name] [color]

import sys
import cv2
import numpy as np

# def pngEncodeDecode(in_imgs, ch, quality=6):
#     """
#     :param in_imgs: 入力画像リスト
#     :param ch:      出力画像リストのチャンネル数（OpenCV形式）
#     :param quality: 圧縮する品質（0-9）
#     :return:        出力画像リスト
#     """
#
#     encode_param = [int(cv2.IMWRITE_PNG_COMPRESSION), quality]
#     out_imgs = []
#
#     for img in in_imgs:
#         result, encimg = cv2.imencode('.png', img, encode_param)
#         if False == result:
#             print('could not encode image!')
#             exit()
#
#         decimg = cv2.imdecode(encimg, ch)
#         out_imgs.append(decimg)
#
#     return out_imgs

# name = 'dummy'
# width = 200
# height = 100
name = sys.argv[1]
width = sys.argv[2]
height = sys.argv[3]

blank = np.zeros((int(height), int(width), 3))
blank += [0, 0, 0][::-1] # カラーコードを指定

cv2.imwrite(name + '-' + str(width) + 'x' + str(height) + '.png', blank)




# img = cv2.imread(name + '-' + str(width) + 'x' + str(height) + '.png')
# height, width, ch = img.shape
# img = pngEncodeDecode([img], ch, 9)
#
# cv2.imwrite(name + '2-' + str(width) + 'x' + str(height) + '.png', img[0])
