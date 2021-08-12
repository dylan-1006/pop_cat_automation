import pyautogui
x=0
screen_width, screen_height= pyautogui.size()
print(screen_width , screen_height)
pyautogui.moveTo()
current_X_position, current_Y_position =pyautogui.position()
print(current_X_position,current_Y_position)
while x!=1000:
    pyautogui.click(1708,234)
    current_X_position, current_Y_position = pyautogui.position()
    x+=1
    if current_X_position!=  1708 or current_Y_position!= 234:
        break

