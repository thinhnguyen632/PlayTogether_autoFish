from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as agui
from random import randint
import time

def detectFish(imgCrop):
    mask = cv.threshold(imgCrop, 250, 255, cv.THRESH_BINARY)[1]
    # cv.imshow('roi', mask)
    if np.sum(mask) != 0:
        return 1
    else:
        return 0

def pullRod():
    agui.press('space') # keo can
    time.sleep(6)
    agui.press('0') # bao quan ca
    time.sleep(2)
    agui.press('9') # cua xe hong =))
    time.sleep(2)
    agui.press('4') # bat dau cau
    return

def selectRod():
    time.sleep(2)
    agui.press('1') # mo tui
    time.sleep(2)
    agui.press('2') # chon tab can cau
    time.sleep(2)
    agui.press('3') # chon can cau
    time.sleep(2)
    agui.press('4') # bat dau cau
    return

def repairRod():
    time.sleep(2)
    agui.press('1') # mo tui
    time.sleep(2)
    agui.press('2') # chon tab can cau
    time.sleep(2)
    agui.press('8') # sua can cau
    time.sleep(2)
    agui.press('7') # chon gia tien
    time.sleep(2)
    agui.press('7') # dong y
    time.sleep(2)
    agui.press('7') # ra ngoai
    time.sleep(2)
    agui.press('4') # tiep tuc cau
    return

def selectROI():
    # select ROI
    time.sleep(3)
    img = agui.screenshot()
    img = np.array(img)
    r = cv.selectROI(img)
    cv.destroyAllWindows()
    return r

# huong dan setting gia lap
print('SETTING KEYBOARD MAPPING')
print('[1]: tui do')
print('[2]: tab cau ca')
print('[3]: can cau (nen dat o vi tri can cau 1-3)')
print('[4]: bat dau cau')
print('[0]: bao quan')
print('[9]: bao quan cua xe hong =))')
print('[8]: sua can cau')
print('[7]: dong y sua can cau')
print('Ctrl + c de dung auto')

# nhap do phan giai cua man hinh (1920x1080)
print('Nhap do phan giai cua man hinh (w, h): ')
width = input()
height = input()
x, y, w, h = (0, 0, width, height)

# nhap do ben vao day
print('Nhap do ben toi da cua can cau: ')
max_dura = int(input())
print('Nhap do ben hien tai cua can cau: ')
init_dura = int(input())

time.sleep(2)
selectRod()
r = selectROI()

init = 0
curr_dura = init_dura
fishing = 1

while(True):
    img = agui.screenshot() #capturing screenshot
    frame = np.array(img) #converting the image into numpy array representation 
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #converting the BGR image into GRAY image
    imgCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    if fishing == 1:    
        if curr_dura == 0:
            repairRod()
            curr_dura = max_dura

        if init == 0:
            result = detectFish(imgCrop)
            if result == 1:
                pullRod()
                init = 1
                fishing = 0
            else:
                fishing = 2
        
        else:
            result = detectFish(imgCrop)
            if result == 1:
                pullRod()
                fishing = 0
            else:
                fishing = 2
            
    if fishing == 0:
        agui.press('4')
        curr_dura = curr_dura - 1
        fishing = 1

    if fishing == 2:
        fishing = 1

    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()