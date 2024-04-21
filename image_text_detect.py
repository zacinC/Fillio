import PIL.ImageGrab
import pytesseract
import PIL.Image
import PIL
import keyboard
import time
import os
import cv2
import easyocr


current_time = current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

keyboard.send('PrtScn')
time.sleep(6) #U koliko ne bi stavili sleep algoritam bi nastavio da se izvrsava

clipboard_image = PIL.ImageGrab.grabclipboard()
clipboard_image.save(f'message_{current_time}.png')

time.sleep(1)

#-----------Ukoliko se koristi pytesseract------------
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
myconfig = r'--psm 6 --oem 3'
text = pytesseract.image_to_string(PIL.Image.open(f'message_{current_time}.png'), config=myconfig)
os.remove(f'message_{current_time}.png')
text = text.strip()
print(text)


#-----------Ukoliko se koristi cv2 i easyocr-----------
#img = cv2.imread(f'message_{current_time}.png')
#reader = easyocr.Reader(['en'])
#text = reader.readtext(img)
#os.remove(f'message_{current_time}.png')

#for t in text:
 #   print(t[1].strip())