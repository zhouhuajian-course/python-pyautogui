"""
pyautogui 鼠标滚动

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import scroll, vscroll, hscroll, moveTo

"""
主要内容：
1. scroll()  - 鼠标垂直滚动；
2. vscroll() - 鼠标垂直滚动；
3. hscroll() - 鼠标水平滚动。
"""


def test_scroll():
    """鼠标滚动"""
    # The amount of scrolling in a “click” varies between platforms.
    # scroll(1)  # win10，滚轮向上滚动
    # scroll(1000)  # win10，滚轮向上滚动
    #  1 10 100 1000
    # scroll(-1000)  # win10，滚轮向下滚动
    # -1 -10 -100 -1000
    # 可多尝试确定具体的参数值

    # win10，有bug，并没有做鼠标移动的逻辑
    # 可单独写moveTo
    # scroll(50, 726, 618)  # position()
    # moveTo(726, 618)
    # scroll(50)

    # vscroll()  # vertical 和scroll功能一样
    # hscroll()  # horizontal Linux和苹果系统才支持


test_scroll()
