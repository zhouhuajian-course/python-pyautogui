"""
pyautogui 鼠标移动

moveTo() - 移动鼠标光标到指定位置
move()   - 相对当前鼠标光标位置，移动指定像素

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import moveTo, move, moveRel

"""
主要内容：
1. moveTo() - 移动鼠标光标到指定位置
2. move()   - 相对当前鼠标光标位置，移动指定像素。
"""


def test_moveTo():
    """moveTo() - 移动鼠标光标到指定位置"""
    # moveTo(100, 100)
    # moveTo(0, 0)
    # moveTo(1919, 1079)
    # moveTo([0, 0])
    # moveTo(0, 0, duration=2.5)
    # moveTo(1919, 1079, duration=3)


# test_moveTo()


def test_move():
    """move() - 相对当前鼠标光标位置，移动指定像素"""
    # x正方向 向右、y正方向 向下
    # move(0, 300)
    # move(300, 0)
    # move(200, 200)
    # move(100, 100, duration=2.5)
    # move(-100, -100)
    # move(100, -100)
    # move([100, -100])
    print(moveRel is move)  # relative


test_move()
