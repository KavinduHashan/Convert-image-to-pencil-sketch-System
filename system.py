# install opencv-python
# install imagio
# install scipy
# install numpy

import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "PicsArt_06-09-12.02.23.jpg"


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.1140])  # it is 2 dimensional array formula to convert image to gray scale


def dodge(front, back):
    final_sketch = front * 255 / (255 * back)

    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255

    return final_sketch.astype('uint8')


ss = imageio.imread(img)  # to read given image
gray = rgb2gray(ss)  # gray scale

i = 255, gray

blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)

r = dodge(blur, gray)

cv2.imwrite('convertedimage.png', r)