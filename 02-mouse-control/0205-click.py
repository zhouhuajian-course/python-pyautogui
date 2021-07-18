"""
pyautogui 鼠标点击

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import click, leftClick, middleClick, rightClick, doubleClick, tripleClick, easeInBack, moveTo, PRIMARY, \
    SECONDARY, LEFT, MIDDLE, RIGHT

"""
主要内容：
1. click()       - 鼠标点击；
2. leftClick()   - 鼠标左键点击一次。
3. middleClick() - 鼠标中键点击一次。
4. rightClick()  - 鼠标右键点击一次。
5. doubleClick() - 鼠标点击两次；
6. tripleClick() - 鼠标点击三次。
"""


def test_click():
    """鼠标点击"""
    # click()
    # click(57, 511)  # position
    # click(57, 511, duration=2, tween=easeInBack)
    # moveTo(57, 511, duration=2, tween=easeInBack)
    # click(clicks=2, interval=0.0, button=LEFT)
    # click(clicks=2, interval=0.2, button=LEFT)
    # 注意点：间隔过长，系统会认为是两次单击，而不是双击
    # click(clicks=2, interval=1, button=LEFT)
    # click(clicks=3, interval=0.3)  # 演示Pycharm三击一行
    # click(button=RIGHT)

    # 2. leftClick()   - 鼠标左键点击一次。
    # leftClick()  # 比click()少2个参数，button固定为LEFT，clicks固定为1 便捷函数
    # 3. middleClick() - 鼠标中键点击一次。
    # middleClick() # 便捷函数
    # 4. rightClick()  - 鼠标右键点击一次。
    # rightClick()  # 便捷函数
    # 5. doubleClick() - 鼠标点击两次；
    # doubleClick()  # 比click()少1个参数，clicks固定为2 便捷函数
    # 6. tripleClick() - 鼠标点击三次。
    # tripleClick(interval=0.3)  # clicks固定为3 便捷函数


test_click()
