import PIL.ImageGrab
import pytesseract
import PIL.Image
import PIL
import keyboard
import time
import os


def screenshot_to_text():
    current_time = current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

    clipboard_original_content = PIL.ImageGrab.grabclipboard()
    clipboard_current_content = PIL.ImageGrab.grabclipboard()

    keyboard.send('shift+win+s')

    start_time = time.time()

    while clipboard_original_content == clipboard_current_content and time.time() - start_time < 7:
        clipboard_current_content = PIL.ImageGrab.grabclipboard()

    if clipboard_current_content == clipboard_original_content:
        return -1

    clipboard_current_content.save(f'message_{current_time}.png')

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    myconfig = r'--psm 6 --oem 3'
    text = pytesseract.image_to_string(PIL.Image.open(
        f'message_{current_time}.png'), config=myconfig, lang='srp_latn')
    os.remove(f'message_{current_time}.png')
    text = text.strip()
    return text
