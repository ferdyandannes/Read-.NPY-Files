from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import cv2
import os
import glob

data_dir = "D:/Kuliah/S2/"
npy_dir = os.path.join(data_dir, 'Depth/')
npy_files = os.listdir(npy_dir)
npy_files.sort()
total_npy = glob.glob(npy_dir + '*.npy')

for npy in range(len(total_npy)):
    npys = os.path.join(npy_dir, str(npy).zfill(4) + '.npy')
    print(npys)
    img_array = np.load(npys)
    cv2.imshow("a", img_array)
    cv2.waitKey(0)
