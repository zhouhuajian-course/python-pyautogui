"""
pyautogui 按快捷键（热键） shortcut hotkey

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import hotkey, keyDown, keyUp

"""
主要内容：
1. hotkey - 按快捷键（热键）。
"""


def test_hotkey():
    """按快捷键（热键）"""
    # 快捷键ctrl+v
    # 复制123456
    # keyDown('ctrl')
    # keyDown('v')
    # keyUp('v')
    # keyUp('ctrl')
    # 可以使用hotkey一行代码实现
    # hotkey('ctrl', 'v')

    # def hotkey(*args, **kwargs):
    #     print(args, kwargs)
    # hotkey('ctrl', 'v', interval=0.2, logScreenshot=False)
    # hotkey(['ctrl', 'v'])  # 不能传列表
    # hotkey(*['ctrl', 'v'])

    # hotkey('ctrl', 'v', interval=0.2)  # interval参数意义不大
    # hotkey('ctrl', 'v', interval=2)

    # hotkey("ctrl", "alt", "s")  # Pycharm 设置               setting
    # hotkey("win", "d")          # Windows 徽标键 + D 显示桌面 desktop


test_hotkey()
