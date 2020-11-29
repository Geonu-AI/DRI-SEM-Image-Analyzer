from scipy import ndimage

def GausianFiltration(ImageArray):
    SEM_Image_GaussianFilter = ndimage.gaussian_filter(ImageArray, sigma=1.5)
    return SEM_Image_GaussianFilter

def MedianFiltration(ImageArray):
    SEM_Image_MedianFilter = ndimage.median_filter(ImageArray, size = 5)
    return SEM_Image_MedianFilter
