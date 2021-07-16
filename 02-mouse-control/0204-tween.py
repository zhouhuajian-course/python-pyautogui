"""
pyautogui 鼠标移动/拖拽 补间动画/过渡效果

@author  : zhouhuajian
@version : v1.0
"""

from pyautogui import moveTo, move, dragTo, drag, linear, easeInQuad, easeOutQuad, easeInOutQuad, easeInElastic, easeOutElastic, easeInOutElastic, easeInBack, easeOutBack, easeInOutBack

"""
主要内容：
鼠标移动/拖拽 补间动画/过渡效果；
"""


def test_tween():
    """鼠标移动/拖拽 补间动画/过渡效果"""
    # moveTo(179, 954, duration=2, tween=linear)
    # moveTo(179, 954, duration=2, tween=easeInQuad)
    """
    ease-in     规定以慢速开始的过渡效果  
    ease-out    规定以慢速结束的过渡效果
    ease-in-out 规定以慢速开始和结束的过渡效果
    """
    # moveTo(179, 954, duration=2, tween=easeOutQuad)
    # moveTo(179, 954, duration=2, tween=easeInOutQuad)
    # move(500, 500, duration=2, tween=easeInElastic)
    # move(500, 500, duration=2, tween=easeOutElastic)
    # move(500, 500, duration=2, tween=easeInOutElastic)
    # drag(0, 300, duration=2, tween=easeInBack)
    # drag(0, 300, duration=2, tween=easeOutBack)
    # drag(0, 300, duration=2, tween=easeInOutBack)
    def custom_tween(n):
        # print(n) # 0.0 <= n < 1.0
        # return n
        if n < 0.2:
            # return -0.2
            return 0.2
        elif 0.2 <= n < 0.5:
            return 0.5
        else:
            return n
    move(0, 500, duration=2, tween=custom_tween)


test_tween()


