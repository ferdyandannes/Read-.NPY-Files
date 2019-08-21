from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import cv2

img_array = np.load('0000.npy')
print(img_array.shape)

cv2.imshow("a", img_array)
cv2.waitKey(0)