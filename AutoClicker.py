import time
import mouse
import keyboard
import random
import threading
import sys
import signal
from wx.adv import TaskBarIcon
from wx import App, Icon

isOn = False
isOn2 = False

isCtrlOn = False

wxApp = App()

print("Welcome to AutoClicker 2000 !")
print("Remember, use CTRL + I to toggle the left click autoclicker on or off")
print("Remember, use CTRL + O to toggle the right click autoclicker on or off")
print("And use CTRL + C to stop.")

calcClickPerSeconds = 1 / int(input("Enter the number of CPS you want: "))


def update_icon():
    global taskbarIcon, isOn, isOn2
    if not isOn and not isOn2:
        taskbarIcon.SetIcon(Icon("not_used.ico"), "AutoClicker2000")
    if isOn and not isOn2:
        taskbarIcon.SetIcon(Icon("used_left.ico"), "AutoClicker2000")
    if not isOn and isOn2:
        taskbarIcon.SetIcon(Icon("used_right.ico"), "AutoClicker2000")
    if isOn and isOn2:
        taskbarIcon.SetIcon(Icon("used_both.ico"), "AutoClicker2000")

def signal_handler(sig, frame):
    print("Stopping program...")
    taskbarIcon.Destroy()
    sys.exit(0)

def ctrlOnCallback(val):
    global isCtrlOn
    isCtrlOn = True

def ctrlOffCallback(val):
    global isCtrlOn
    isCtrlOn = False

def lcThread():
    global isOn
    time_ = time.time()
    while isOn:
        while not time.time()>=time_+calcClickPerSeconds:
            pass
        mouse.click('left')
        time_ = time_ + calcClickPerSeconds
def rcThread():
    global isOn2
    time_ = time.time()
    while isOn2:
        while not time.time()>=time_+calcClickPerSeconds:
            pass
        mouse.click('right')
        time_ = time_ + calcClickPerSeconds

def tryLc(val):
    global isCtrlOn, isOn
    if isCtrlOn:
        isOn = not isOn
        update_icon()
        if isOn:
            lcThreadOb = threading.Thread(target=lcThread)
            lcThreadOb.start()
def tryRc(val):
    global isCtrlOn, isOn2
    if isCtrlOn:
        isOn2 = not isOn2
        update_icon()
        if isOn2:
            rcThreadOb = threading.Thread(target=rcThread)
            rcThreadOb.start()

keyboard.on_press_key(key='control', callback=ctrlOnCallback)
keyboard.on_release_key(key='control', callback=ctrlOffCallback)

keyboard.on_press_key(key='i', callback=tryLc)
keyboard.on_release_key(key='o', callback=tryRc)

signalevent = signal.signal(signal.SIGINT, signal_handler)

taskbarIcon = TaskBarIcon()
taskbarIcon.SetIcon(Icon("not_used.ico"), "AutoClicker2000")

while True:
    time.sleep(60)