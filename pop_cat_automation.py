import pyautogui
#run the below two lines and get the coordinates of the postion to click 
current_X_position, current_Y_position =pyautogui.position() 
print(current_X_position,current_Y_position)

count=0
while count!=1000: #set value for amount of times to click
    pyautogui.click(1708,234) #insert (X,Y) coordinates obtained from above
    current_X_position, current_Y_position = pyautogui.position()
    x+=1
    if current_X_position!=  1708 or current_Y_position!= 234: 
        #insert (X,Y) coordinates obtained from above, this will stop the loop when u move ur mouse
        break

