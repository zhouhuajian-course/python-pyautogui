"""
pyautogui 屏幕截图

@author  : zhouhuajian
@version : v1.0
"""

import pyautogui
from pyautogui import screenshot, moveTo, dragTo, click, press
from PIL.Image import Image

"""
主要内容：
1. screenshot() - 屏幕截图；
2. 其他函数logScreenshot屏幕截图日志参数；
3. 屏幕截图日志相关常量。
"""


def test_screenshot():
    """screenshot() - 屏幕截图"""
    # img = screenshot()
    # print(img)
    # print(type(img), type(img) is Image)
    # img.save("./1.png")
    # box = (12, 276, 116, 717)  # position
    # img.crop(box).save('./2.jpg')

    # print(screenshot(imageFilename='./3.png'))
    # box = (12, 276, 116 - 12, 717 - 276)
    # print(screenshot(imageFilename='./4.jpg', region=box))

    # moveTo, dragTo, click ...
    # moveTo((100, 100), logScreenshot=True)
    # click(logScreenshot=True)
    # press('space', logScreenshot=True)

    # 删掉之前截图
    # pyautogui.LOG_SCREENSHOTS = True
    # moveTo((100, 100))
    # click()
    # press('space')

    # 删掉之前截图
    # pyautogui.LOG_SCREENSHOTS_LIMIT = 2
    # press('1', logScreenshot=True)
    # press('2', logScreenshot=True)
    # press('3', logScreenshot=True)


test_screenshot()
