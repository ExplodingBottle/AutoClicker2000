import time
import mouse
import keyboard
import random
import threading
import sys
import signal

isOn = False
isOn2 = False

isCtrlOn = False

print("Welcome to AutoClicker 2000 !")
print("Remember, use CTRL + I to toggle the left click autoclicker on or off")
print("Remember, use CTRL + O to toggle the right click autoclicker on or off")
print("And use CTRL + C to stop.")
calcClickPerSeconds = 1 / int(input("Enter the number of CPS you want: "))

def signal_handler(sig, frame):
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
        time.sleep(0.9)
        if isOn:
            lcThreadOb.start()
def tryRc(val):
    global isCtrlOn, isOn2
    if isCtrlOn:
        isOn2 = not isOn2
        time.sleep(0.9)
        if isOn2:
            rcThreadOb.start()

lcThreadOb = threading.Thread(target=lcThread)
rcThreadOb = threading.Thread(target=rcThread)

keyboard.on_press_key(key='control', callback=ctrlOnCallback)
keyboard.on_release_key(key='control', callback=ctrlOffCallback)

keyboard.on_press_key(key='i', callback=tryLc)
keyboard.on_release_key(key='o', callback=tryRc)

signalevent = signal.signal(signal.SIGINT, signal_handler)

while True:
    time.sleep(100)