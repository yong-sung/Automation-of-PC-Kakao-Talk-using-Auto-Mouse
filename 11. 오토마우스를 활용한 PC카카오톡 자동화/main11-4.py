import pyautogui
import pyperclip
import time
import schedule

def send_message():
    try:
        pic_position = pyautogui.locateOnScreen(r'11. 오토마우스를 활용한 PC카카오톡 자동화\카카오톡_내사진1.png')
        
        if pic_position:
            click_position = pyautogui.center(pic_position)
            pyautogui.doubleClick(click_position)

            pyperclip.copy("이것은 자동화된 메시지입니다.")
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1.0)

            pyautogui.write(["enter"])
            time.sleep(1.0)

            pyautogui.write(["escape"])
            time.sleep(1.0)
        else:
            print("화면에서 이미지를 찾을 수 없습니다.")

    except Exception as e:
        print("오류가 발생했습니다:", e)

# 작업을 10초마다 예약합니다
schedule.every(10).seconds.do(send_message)

# 예약된 작업을 실행하는 무한 루프
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print("스크립트가 중단되었습니다.")
        break
