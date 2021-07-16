"""
pyautogui 键盘控制

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import press, keyDown, keyUp, write, KEYBOARD_KEYS

"""
主要内容：
1. press()   - 按键盘按键(按下并且释放)；
2. keyDown() - 按键盘按键(按下但不释放)；
2. keyUp()   - 释放已按下的键盘按键。
"""


def test_press_keyDown_keyUp():
    """按键盘按键"""
    # press('a')
    # press('space')
    # press(['#', 'a', 'space', 'A', ' ', '1'])
    # KEYBOARD_KEYS
    # 注意：这里的interval是重复按的时间间隔，不是按列表里每个键的时间间隔
    # press(['a', 'b', 'c'])
    # press(['a', 'b', 'c'], interval=1)
    # write
    # press(['a', 'b', 'c'], presses=3, interval=1)
    # press('a', presses=3, interval=1)

    # 不是键盘按键，也就是KEYBOARD_KEYS或KEY_NAMES没有的按键
    # 会被直接忽略。
    # press('©')  # 忽略的源码简单讲解一下


    # press('a')等价于
    # keyDown('a')
    # keyUp('a')

    # 演示快捷键ctrl+v
    # 复制123456
    keyDown('ctrl')
    keyDown('v')
    keyUp('v')
    keyUp('ctrl')


test_press_keyDown_keyUp()
