import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('robin.jpg',1)

color=('b','g','r')

for i,col in enumerate(color):
    histogram=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histogram,color=col)
    plt.xlim([0,256])

plt.show()
