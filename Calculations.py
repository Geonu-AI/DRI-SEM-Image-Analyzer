import numpy as np

def DRIcalculations(Histogram):

    # print(np.sum(Histogram_SEM_Image1_GaussianFilter[:200]) / np.sum(Histogram_SEM_Image1_GaussianFilter))

    Pores = Histogram <= 80
    Gangues = np.logical_and(Histogram > 80, Histogram <= 130)
    IronOx = np.logical_and(Histogram > 130, Histogram <= 150)
    Iron = Histogram >= 150

    porecount = np.sum(Histogram[:80]) / np.sum(Histogram)
    ganguecount = np.sum(Histogram[80:130]) / np.sum(Histogram)
    ironoxcount = np.sum(Histogram[130:150]) / np.sum(Histogram)
    ironcount = np.sum(Histogram[150:]) / np.sum(Histogram)

    # ganguecount = np.count_nonzero(Gangues)
    # ironoxcount = np.count_nonzero(IronOx)
    # ironcount = np.count_nonzero(Iron)

    return porecount, ganguecount, ironoxcount, ironcount