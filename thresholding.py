from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as agui
import time
import matplotlib.pyplot as plt

# Read image
im = cv.imread("a.png", cv.IMREAD_COLOR)

# Select ROI
r = cv.selectROI(im)

# Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# # gaussian filter
# imCrop = cv.GaussianBlur(imCrop, (3,3), 0)

# # chuyen sang khong gian mau hsv
# hsv = cv.cvtColor(imCrop, cv.COLOR_BGR2HSV)
# lower_white = np.array([0,0,0], dtype=np.uint8)
# upper_white = np.array([0,0,255], dtype=np.uint8)

# # Threshold the HSV image to get only white colors
# mask = cv.inRange(hsv, lower_white, upper_white)

# kernel_ci = np.array([[0,0,1,0,0],
#                         [0,1,1,1,0],
#                         [1,1,1,1,1],
#                         [0,1,1,1,0],
#                         [0,0,1,0,0]], dtype = np.uint8)
# mask = cv.morphologyEx(mask, cv.MORPH_ERODE, kernel_ci, iterations = 3)
# mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel_ci, iterations = 4)

# # find contours
# contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# object = np.empty((0, 4), dtype=np.uint8)
# for c in contours:
#     area = cv.contourArea(c)
#     x, y, w, h = cv.boundingRect(c)
#     cv.rectangle(im,(x + r[0], y + r[1]), (x + w + r[0], y + h + r[1]),(0,255,0),2)
#     object = np.vstack((object, np.array([x + 420, y + 100, w, h])))

# print(object.shape[0])

gray = cv.cvtColor(imCrop, cv.COLOR_BGR2GRAY)
mask = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)[1]

print(np.sum(gray))

# Display cropped image
cv.imshow("Image", mask)
cv.waitKey(0)
cv.destroyAllWindows()