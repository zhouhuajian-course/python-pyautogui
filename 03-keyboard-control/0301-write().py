"""
pyautogui 批量按键盘按键

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import write, typewrite, KEYBOARD_KEYS, KEY_NAMES

"""
主要内容：
1. write()     - 批量按键盘按键;
2. typewrite() - 批量按键盘按键。
"""


def test_write():
    """批量按键盘按键"""
    # write("a")
    # write("abcd1234")
    # write("abcd1234", interval=0.5)
    # 单字符键盘按键 single-character key
    # write("abcdABCD1234\t\n!?#@", interval=0.5)
    # print(len('\t'))
    # print(len('f1'))
    # write("f1", interval=0.5)

    # 不是键盘按键，也就是KEYBOARD_KEYS或KEY_NAMES没有的按键
    # 会被直接忽略。
    # KEYBOARD_KEYS
    # 注意：大写A-Z虽然KEYBOARD_KEYS没有，但可以。在源码中会动态添加。
    # write("abcdABCD©©©©1234", interval=0.5)
    # keyboardMapping = dict([(key, None) for key in KEY_NAMES])
    # print(keyboardMapping)
    # print([chr(num) for num in range(32, 128)])

    # write(['a', 'b', 'c', '1', '2', '3'], interval=0.5)

    # 官网描述不太正确 列表形式参数可以传多字符键盘按键
    # write('abcspace123enter', interval=0.5)
    # write(['a', 'b', 'c', 'space', '1', '2', '3', 'enter'], interval=0.5)
    # write('f1', interval=0.5)
    # write(['f1'])
    print(typewrite == write)


test_write()
