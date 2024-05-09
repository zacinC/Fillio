import PIL.ImageGrab
import pytesseract
import PIL.Image
import PIL
import keyboard
import time
import os
import time
import threading
from pynput import mouse



def on_click(x, y, button, pressed):
    global start_time
    if pressed:
        start_time = time.time()
    else:
        if time.time() - start_time <0.3:
           stop_mouse_listener()


def monitor_mouse():
    global listener
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()


def stop_mouse_listener():
    global listener
    if listener:
        listener.stop()


def screenshot_to_text():

    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

    clipboard_original_content = PIL.ImageGrab.grabclipboard()
    keyboard.send('shift+win+s')

    mouse_thread = threading.Thread(target=monitor_mouse)
    mouse_thread.daemon = True
    mouse_thread.start()

    while True:

        if keyboard.is_pressed('esc'):
            return -1
        
        if mouse_thread.is_alive() == False:
           return -1

        clipboard_current_content = PIL.ImageGrab.grabclipboard()

        if clipboard_original_content != clipboard_current_content:
            break
        
    
    clipboard_image = PIL.ImageGrab.grabclipboard()
    clipboard_image.save(f'message_{current_time}.png')

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    myconfig = r'--psm 6 --oem 3'
    text = pytesseract.image_to_string(PIL.Image.open(
        f'message_{current_time}.png'), config=myconfig, lang='srp_latn')
    os.remove(f'message_{current_time}.png')
    text = text.strip()
    return text
