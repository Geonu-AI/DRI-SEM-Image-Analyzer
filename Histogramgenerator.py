import numpy as np

def histogramgenerator(ArrayImage):

    Histogram_SEM_Filtered, bins2 = np.histogram(ArrayImage, bins=np.arange(257))
    return Histogram_SEM_Filtered
