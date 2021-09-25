import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pyautogui as agui
import time

# # Read image
# img = cv.imread("fixx.jpg", cv.IMREAD_COLOR)

# # Select ROI
# r = cv.selectROI(img)
# cv.destroyAllWindows()

# # Crop image
# imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# # chuyen sang khong gian mau hsv
# hsv = cv.cvtColor(imCrop, cv.COLOR_BGR2HSV)
# h, s, v = cv.split(hsv)

# # Plot histogram
# # hist = cv.calcHist([v], [0], None, [256], [0,255])
# # x = range(256)
# # plt.plot(x,hist)
# # plt.show()

# low_H, high_H = (2, 4)
# low_S, high_S = (170, 173)
# low_V, high_V = (240, 242)

# # Threshold the HSV image
# hsv = cv.inRange(hsv, (low_H, low_S, low_V), (high_H, high_S, high_V))

# print(np.sum(hsv))

# cv.imshow("result", hsv)
# cv.waitKey(0)
# cv.destroyAllWindows()

# select ROI
time.sleep(3)
img = agui.screenshot()
img = np.array(img)
r = cv.selectROI(img)
cv.destroyAllWindows()

img = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
mask = cv.threshold(gray, 97, 255, cv.THRESH_BINARY_INV)[1]
# Plot histogram
hist = cv.calcHist([gray], [0], None, [256], [0,255])
x = range(256)
plt.plot(x,hist)
plt.show()

cv.imshow("result", mask)
cv.waitKey(0)
cv.destroyAllWindows()