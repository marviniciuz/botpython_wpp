import pywhatkit
import keyboard
import time
from datetime import datetime

contacts = [' ',' ']

while len(contacts) >= 1:
    pywhatkit.sendwhatmsg(contacts[0],'ola mundo',datetime.now().hour,datetime.now().minute + 2)

    del contacts[0]
    time.sleep(60)

    keyboard.press_and_release('ctrl + w')