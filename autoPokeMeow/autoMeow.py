import pyautogui as autogui
import time
import cv2 as cv
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Welcome\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

def findPokemon():
    autogui.write(';p')
    autogui.press('enter')

def usePokeball():
    autogui.write('pb')
    autogui.press('enter')

def useGreatball():
    autogui.write('gb')
    autogui.press('enter')

def useUltraball():
    autogui.write('ub')
    autogui.press('enter')

def useMasterball():
    autogui.write('mb')
    autogui.press('enter')

def selectROI():
    # select ROI
    time.sleep(3)
    img = autogui.screenshot()
    img = np.array(img)
    r = cv.selectROI(img)
    cv.destroyAllWindows()
    return r

def detectRarity(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh1 = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
    rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (18, 18))
    dilation = cv.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv.findContours(dilation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    im2 = img.copy()
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
        
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)

    rarity = 0 #Common
    rarity = 1 #Uncommon
    rarity = 2 #Rare
    rarity = 3 #Super Rare
    rarity = 4 #Legendary
    rarity = 5 #Shiny
    return text


box = selectROI()

while(True):
    img_discord = autogui.screenshot() #capturing screenshot
    img_discord = np.array(img_discord) #BGR color space
    img_discord = cv.cvtColor(img_discord, cv.COLOR_BGR2HSV)
    imgCrop_discord = img_discord[int(box[1]):int(box[1]+box[3]), int(box[0]):int(box[0]+box[2])]
   
    gray = cv.cvtColor(imgCrop_discord, cv.COLOR_BGR2GRAY)
    ret, thresh1 = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
    rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (18, 18))
    dilation = cv.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv.findContours(dilation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    im2 = imgCrop_discord.copy()

    file = open("box.txt", "w+")
    file.write("")
    file.close()

    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
        
        # Open the file in append mode
        file = open("box.txt", "a")
        
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)

        # Appending the text into file
        file.write(text)
        file.write("\n")
        
        # Close the file
        file.close
