from PIL import ImageGrab
import cv2 as cv
import numpy as np
from numpy.core.defchararray import split
import pyautogui as agui
from random import randint
import time
import matplotlib.pyplot as plt

time.sleep(4)
img = agui.screenshot()
img = np.array(img)
r = cv.selectROI(img)
cv.destroyAllWindows()

while(True):
    img = agui.screenshot()
    img = np.array(img) #BGR color space
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    imgCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    h, s, v = cv.split(imgCrop)

    # hist = cv.calcHist([v], [0], None, [256], [0,255])
    # x = range(256)
    # plt.plot(x,hist)
    # plt.show()

    low_h, high_h = (10, 30)
    low_s, high_s = (190, 250)
    low_v, high_v = (100, 130)

    kernel = np.array([[0,1,0],
                        [1,1,1],
                        [0,1,0]], dtype = np.uint8)

    mask = cv.inRange(imgCrop, (low_h, low_s, low_v), (high_h, high_s, high_v))

    # h = cv.threshold(h, 50, 255, cv.THRESH_BINARY)[1]
    h = cv.adaptiveThreshold(h, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 1)
    
    cv.imshow("ROI", h)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
