from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as agui
from random import randint
import time

def detectFish(gray):
    mask = cv.threshold(gray, 250, 255, cv.THRESH_BINARY)[1]
    if np.sum(mask) != 0:
        return 1
    else:
        return 0

def detectFix(gray):
    mask = cv.threshold(gray, 97, 255, cv.THRESH_BINARY_INV)[1]
    if np.sum(mask) != 0:
        return 1
    else:
        return 0

def selectROI():
    # select ROI
    time.sleep(3)
    img = agui.screenshot()
    img = np.array(img)
    r = cv.selectROI(img)
    cv.destroyAllWindows()
    return r

def pullRod(delay):
    agui.press('space') # keo can
    time.sleep(7)
    agui.press('0') # bao quan ca
    time.sleep(delay)
    agui.press('9')
    return

def fixRod(delay):
    time.sleep(delay)
    agui.press('8') # sua can cau
    time.sleep(delay)
    agui.press('7') # chon gia tien
    time.sleep(delay)
    agui.press('7') # dong y
    time.sleep(delay)
    agui.press('7') # ra ngoai
    return

def init(init_dura, fishing_init, delay):
    time.sleep(delay)
    agui.press('1') # mo tui
    time.sleep(delay)
    agui.press('2') # chon tab can cau
    time.sleep(delay)
    r_fix = selectROI()
    time.sleep(delay)
    agui.press('3') # chon can cau
    time.sleep(delay)
    agui.press('4') # bat dau cau
    time.sleep(delay)
    r_fish = selectROI()
    curr_dura = init_dura
    fishing = fishing_init
    return r_fix, r_fish, curr_dura, fishing

def intro():
    # huong dan setting gia lap
    print('SETTING KEYBOARD MAPPING')
    print('[1]: tui do')
    print('[2]: tab cau ca')
    print('[3]: can cau')
    print('[4]: bat dau cau')
    print('[0]: bao quan')
    print('[9]: bao quan cua xe hong =))')
    print('[8]: sua can cau')
    print('[7]: dong y sua can cau')
    print('Ctrl + c de dung auto')
    print('Kame')
    return

# intro
intro()

# nhap cac input
print('Nhap delay (2 hoac >=1): ')
delay = int(input())
print('Nhap timeout watchdog (2000 hoac >= 1000),: ')
wd = int(input())
print('Nhap do ben toi da cua can cau: ')
max_dura = int(input())
print('Nhap do ben hien tai cua can cau: ')
init_dura = int(input())

# bat dau
r_fix, r_fish, curr_dura, fishing = init(init_dura, 1, delay)

print("Do ben ban dau:" + str(curr_dura))
watchdog = 0

while(True):
    img_fish = agui.screenshot() #capturing screenshot
    img_fish = np.array(img_fish) #BGR color space
    img_fish = cv.cvtColor(img_fish, cv.COLOR_BGR2GRAY)
    imgCrop_fish = img_fish[int(r_fish[1]):int(r_fish[1]+r_fish[3]), int(r_fish[0]):int(r_fish[0]+r_fish[2])]

    if fishing == 1:
        result_fish = detectFish(imgCrop_fish)
        if result_fish == 1:
            print("Phat hien [!], keo can!")
            pullRod(delay)
            curr_dura = curr_dura - 1
            print("Do ben hien tai: " + str(curr_dura))
            print("Watchdog: " + str(watchdog))
            watchdog = 0
            fishing = 0
            result_fish = 0

    if fishing == 0:
        if curr_dura == 0:
            print("Kiem tra do ben...")
            time.sleep(delay)
            agui.press('1') # mo tui
            time.sleep(delay)
            agui.press('2') # chon tab can cau
            time.sleep(delay)
            img_fix = agui.screenshot()
            img_fix = np.array(img_fix)
            img_fix = cv.cvtColor(img_fix, cv.COLOR_BGR2GRAY)
            imgCrop_fix = img_fix[int(r_fix[1]):int(r_fix[1]+r_fix[3]), int(r_fix[0]):int(r_fix[0]+r_fix[2])]
            result_fix = detectFix(imgCrop_fix)

            if result_fix == 1:
                fixRod(delay)
                curr_dura = max_dura
                print("Sua can cau thanh cong")
                print("Do ben hien tai: " + str(curr_dura))

            else:
                time.sleep(delay)
                agui.press('7') # ra ngoai
                curr_dura = curr_dura + 1
                print("Sua can cau khong thanh cong, thoat")
                print("Do ben hien tai: " + str(curr_dura))

        print("Tiep tuc cau...")
        time.sleep(delay)
        agui.press('4') # tiep tuc cau

    watchdog = watchdog + 1
    fishing = 1
    
    if watchdog > wd:
        print("Timeout!")
        curr_dura = 0
        fishing = 0
        watchdog = 0

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()