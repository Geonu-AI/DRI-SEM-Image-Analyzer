# Other than basic modules below, also need 'Pillow' module installed to view images.
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

# Read an image as an array
SEM_Image1 = plt.imread('Picture1_Noisy.jpg')

# Removing scale bars and experimental parameters
SEM_Image1_ArrayRemoved = SEM_Image1[:350,:400]

plt.figure()
plt.imshow(SEM_Image1_ArrayRemoved)
plt.show()

SEM_Image1_GaussianFilter = ndimage.gaussian_filter(SEM_Image1_ArrayRemoved, sigma = 1.5)
plt.figure()
plt.imshow(SEM_Image1_GaussianFilter)
plt.show()

SEM_Image1_MedianFilter = ndimage.median_filter(SEM_Image1_ArrayRemoved, size = 5)
plt.figure()
plt.imshow(SEM_Image1_MedianFilter)
plt.show()

Histogram_SEM_Image1_ArrayRemoved, bins1 = np.histogram(SEM_Image1_ArrayRemoved, bins = np.arange(257))
Histogram_SEM_Image1_GaussianFilter, bins2 = np.histogram(SEM_Image1_GaussianFilter, bins = np.arange(257))
Histogram_SEM_Image1_MedianFilter, bins3 = np.histogram(SEM_Image1_MedianFilter, bins =np.arange(257))

plt.plot(np.arange(256), Histogram_SEM_Image1_ArrayRemoved, color ='blue')
plt.plot(np.arange(256), Histogram_SEM_Image1_GaussianFilter, color ='green')
plt.plot(np.arange(256), Histogram_SEM_Image1_MedianFilter, color= 'red')
plt.show()


print(Histogram_SEM_Image1_GaussianFilter)

print(np.sum(Histogram_SEM_Image1_GaussianFilter[:200])/np.sum(Histogram_SEM_Image1_GaussianFilter))
#
# Pores = Histogram_SEM_Image1_GaussianFilter <= 90
# Gangues = np.logical_and(Histogram_SEM_Image1_GaussianFilter > 90, Histogram_SEM_Image1_GaussianFilter <= 150)
# IronOx = np.logical_and(Histogram_SEM_Image1_GaussianFilter > 150, Histogram_SEM_Image1_GaussianFilter <= 190)
# Iron = Histogram_SEM_Image1_GaussianFilter >= 190
#
# print(np.count_nonzero(Pores))
# print(np.count_nonzero(Gangues))
# print(np.count_nonzero(IronOx))
# print(np.count_nonzero(Iron))

# print(type(Pores))
# phases = Pores.astype(np.int) + 2 * IronOx.astype(np.int) +3 * Gangues.astype(np.int) + 4* Iron.astype(np.int)
# print(phases)
# print(type(phases))