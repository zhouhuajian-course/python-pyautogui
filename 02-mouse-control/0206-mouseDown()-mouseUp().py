"""
pyautogui 鼠标按下、鼠标释放

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import mouseDown, mouseUp, click, dragTo, easeInBack, LEFT, RIGHT

"""
主要内容：
1. mouseDown() - 鼠标按下；
2. mouseUp()   - 鼠标释放。
"""


def test_mouseDown_mouseUp():
    """鼠标按下、鼠标释放"""
    # click()
    # mouseDown()  # 演示火狐 按下 鼠标移动
    # mouseDown(82, 510)
    # 源码duration、tween有bug，对比click源码
    # 可能是作者没测试全
    # mouseDown(82, 510, duration=2, tween=easeInBack)
    # mouseDown()
    # mouseUp()  # 也有duration、tween参数的bug
    # mouseDown(button=LEFT)
    # mouseUp(button=LEFT)
    # 等同于click(button=LEFT)
    # mouseDown(button=RIGHT)
    # mouseUp(button=RIGHT)
    # 等同于click(button=RIGHT)
    # 简单讲一下鼠标点击和鼠标拖拽
    # 与鼠标按下和鼠标抬起的关系


test_mouseDown_mouseUp()
