import random
import time
import pyautogui
import keyboard
ran = {"first" : 0, "second" : 0, "third" : 0}

print("Hold F6 to stop")
time.sleep(1)
pyautogui.typewrite("Let's go gambling")
pyautogui.press("enter")
time.sleep(2)

while True:
    if keyboard.is_pressed("F6"):
        break
    for v in ran:
        ran[v] = random.randint(0,9)
    if ran["first"] == ran["second"] or ran["second"] == ran["third"] or ran["first"] == ran["third"]:
        continue
    time.sleep(2)
    pyautogui.typewrite("X " + str(ran["first"]) + str(ran["second"]) + str(ran["third"]) + " X")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.typewrite("Aww damn it!")
    pyautogui.press("enter")