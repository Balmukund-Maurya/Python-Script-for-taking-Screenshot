from time import sleep
import pyautogui
#delay the screenshot time by 2 sec, so that you can go the desired page you want teh screenshot
for i in range(5):
    sleep(2)
    myScreenshot = pyautogui.screenshot()
    #provide the path to get the screenshot saved
    myScreenshot.save(r"screenshot"+str(i)+".png")
    print("1")

