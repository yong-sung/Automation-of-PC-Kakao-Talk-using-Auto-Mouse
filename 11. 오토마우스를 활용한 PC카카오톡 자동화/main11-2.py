import pyautogui
import pyperclip
import time

picPosition = pyautogui.locateOnScreen(r'11. 오토마우스를 활용한 PC카카오톡 자동화\카카오톡_내사진1.png')
print(picPosition)

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다~~")
pyautogui.hotkey("ctrl", "v")
time.sleep(1.0)

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)