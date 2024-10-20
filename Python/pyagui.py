import pyautogui

x = int(input())

for i in range(1, x+1):

    for j in range(i):
        pyautogui.write("#")

    pyautogui.press("enter")




