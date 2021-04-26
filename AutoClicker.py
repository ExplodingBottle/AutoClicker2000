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

wxApp = App()

print("Welcome to AutoClicker 2000 !")
print("And use CTRL + C to stop.")
keyLeft = input("Enter the key you want to use to toggle on or off AutoClicker2000: ")
keyRight = input("Enter the key you want to use to toggle on or off AutoClicker2000: ")

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
    global isOn
    isOn = not isOn
    update_icon()
    if isOn:
        lcThreadOb = threading.Thread(target=lcThread)
        lcThreadOb.start()

def tryRc(val):
    global isOn2
    isOn2 = not isOn2
    update_icon()
    if isOn2:
        rcThreadOb = threading.Thread(target=rcThread)
        rcThreadOb.start()

keyboard.on_press_key(key=keyLeft, callback=tryLc)
keyboard.on_press_key(key=keyRight, callback=tryRc)

signalevent = signal.signal(signal.SIGINT, signal_handler)

taskbarIcon = TaskBarIcon()
taskbarIcon.SetIcon(Icon("not_used.ico"), "AutoClicker2000")

while True:
    time.sleep(60)