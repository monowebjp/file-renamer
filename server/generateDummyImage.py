# [width] [height] [name] [color]

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

name = 'dummy2'
width = 200
height = 100

blank = np.zeros((height, width, 3))
blank += [0, 0, 0][::-1] # カラーコードを指定

# height, width, ch = blank.shape

# img = pngEncodeDecode([blank], ch, 0)

# cv2.imwrite(name + '-' + str(width) + 'x' + str(height) + '.png', img[0])
cv2.imwrite(name + '-' + str(width) + 'x' + str(height) + '.png', blank)

