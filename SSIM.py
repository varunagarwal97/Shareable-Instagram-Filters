#This code measures the structural similarity between two images

import matplotlib.pyplot as plt
import numpy as np
import pylab
from skimage import measure

a = plt.imread('0.jpg')
b = plt.imread('00.jpg')

ssim = measure.compare_ssim(a,b, multichannel = True)

print (ssim)