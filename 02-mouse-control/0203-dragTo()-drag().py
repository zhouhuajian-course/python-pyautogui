"""
pyautogui 鼠标拖拽

dragTo() - 鼠标拖拽到指定位置
drag()   - 相对当前鼠标光标位置，拖拽指定像素

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import dragTo, drag, dragRel, position, moveTo, mouseDown, LEFT, MIDDLE, RIGHT, Point, mouseUp

"""
主要内容：
1. dragTo() - 鼠标拖拽到指定位置；
2. drag()   - 相对当前鼠标光标位置，拖拽指定像素。
"""


def test_dragTo():
    """dragTo() - 鼠标拖拽到指定位置"""
    # print(position())
    moveTo(63, 496)
    # 注意点：没有持续时间，没拖拽效果。可能系统不支持
    # dragTo(297, 962)
    # dragTo(297, 962, duration=2.5)
    # dragTo([297, 962], duration=5)
    """
    LEFT = "left"
    MIDDLE = "middle"
    RIGHT = "right"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    """
    # dragTo([297, 962], duration=2.5, button=LEFT)
    # dragTo([297, 962], duration=2.5, button=MIDDLE)
    # dragTo([297, 962], duration=2.5, button=RIGHT)
    mouseDown(button=LEFT)
    dragTo([297, 962], duration=2.5, button=LEFT, mouseDownUp=False)
    mouseUp(button=LEFT)


# test_dragTo()


def test_drag():
    """drag() - 相对当前鼠标光标位置，拖拽指定像素"""
    # x正方向 向右、y正方向 向下
    moveTo(63, 496)
    # 注意点：没有持续时间，没拖拽效果。可能系统不支持
    # drag(200, 0)
    # drag(200, 0, duration=2.5)
    # drag(100, 100, duration=2.5)
    # drag([100, 100], duration=2.5)
    # drag([100, 100], duration=2.5, button=LEFT)
    # drag([100, 100], duration=2.5, button=MIDDLE)
    # drag([100, 100], duration=2.5, button=RIGHT)
    print(dragRel is drag)  # relative


test_drag()
