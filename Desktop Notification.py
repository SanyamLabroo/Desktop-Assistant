import os
from win10toast import ToastNotifier
import time

def notification():
    
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()
    title = "Pennywise"
    message = "Hi Sanyam I am Pennywise the Clown." + u"\U0001F921" + "Wanna Play with me."
    
    icon = "icon.ico"
    length = 50
    toast.show_toast(title, message,icon_path=icon, duration=length)

notification()
