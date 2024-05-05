import PIL.ImageGrab
import pytesseract
import PIL.Image
import PIL
import keyboard
import time
import os
import pyautogui

current_time = current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

clipboard_original_content = PIL.ImageGrab.grabclipboard()
keyboard.send('shift+win+s')
# pyautogui.hotkey('shift', 'win', 's')


while True:
    clipboard_current_content = PIL.ImageGrab.grabclipboard()
    if clipboard_original_content != clipboard_current_content:
      #  print("Slika je kopirana u clipboard.")
        break
    # time.sleep(1) čavke

clipboard_image = PIL.ImageGrab.grabclipboard()
# print(clipboard_image)
clipboard_image.save(f'message_{current_time}.png')

# time.sleep(1)

# -----------Ukoliko se koristi pytesseract------------
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
myconfig = r'--psm 6 --oem 3'
text = pytesseract.image_to_string(PIL.Image.open(
    f'message_{current_time}.png'), config=myconfig, lang='srp_latn')
os.remove(f'message_{current_time}.png')
text = text.strip()
print(text)
