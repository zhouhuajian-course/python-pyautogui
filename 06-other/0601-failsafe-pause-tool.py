"""
pyautogui 故障安全、通用暂停、实用工具

@author  : zhouhuajian
@version : v1.0
"""

import pyautogui
from pyautogui import failSafeCheck, FAILSAFE_POINTS, size, position, click, moveTo, mouseInfo, displayMousePosition, \
    sleep, countdown, run, printInfo, getInfo

"""
主要内容：
1. failSafeCheck() - 故障安全检查；
2. 通用暂停；
3. mouseInfo() - 获取鼠标信息工具；
4. displayMousePosition() - 显示鼠标位置工具；
5. sleep() - 休眠；
6. countdown() - 倒计时；
7. run() - 使用迷你语言执行UI自动化操作；
8. printInfo() - 打印UI自动化信息；
9. getInfo() - 获取UI自动化信息。
"""


def test_failSafeCheck():
    """故障安全"""
    # 模拟正在进行很多自动化操作
    # while True:
    #     click(500, 500)
    #     sleep(0.5)

    # print(FAILSAFE_POINTS)

    # failSafeCheck()  # 屏幕四个角落

    # pyautogui.FAILSAFE = False
    # failSafeCheck()




test_failSafeCheck()


def test_pause():
    """通用暂停"""
    # moveTo(500, 500)
    # moveTo(1000, 500)

    # moveTo(500, 500, _pause=False)
    # moveTo(1000, 500, _pause=False)

    # pyautogui.PAUSE = 5
    # moveTo(500, 500)
    # moveTo(1000, 500)
    # print("结束")


test_pause()


def test_tool():
    """实用工具"""
    # mouseInfo()

    # NOTE: 需要在终端运行
    # displayMousePosition()

    # sleep(5)
    # print("结束")

    # print("UI自动化将在5秒后开始")
    # countdown(5)
    # print("...")

    # run('g300,300s2csss2g+500,+0s2rss')
    # screenshot_count = [100]
    # run('g300,300 s2 c ss s2 g+500,+0 s2 r ss', _ssCount=screenshot_count)
    # print(screenshot_count)

    # printInfo()

    # print(getInfo())

    info = printInfo(dontPrint=True)
    print(info)


test_tool()
