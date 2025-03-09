import pygetwindow as gw
import psutil
from pynput.keyboard import Key, Controller
from time import sleep
import tkinter as tk

windows = gw.getWindowsWithTitle("Edge")

for win in windows:
    win.activate()
    sleep(1)
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press("l")
        keyboard.release("l")
        keyboard.press("c")
        keyboard.release("c")

    url = tk.Tk().clipboard_get()

    print(url)